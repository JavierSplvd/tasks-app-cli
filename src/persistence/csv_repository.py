import csv
import os
from entities.task import Task


# This class uses the Singleton pattern.
class CsvRepository:
    __instance = None
    # save in the HOME directory
    home = os.path.expanduser("~")
    csv_filename: str = home + "/task-manager.csv"

    @staticmethod
    def get_instance():
        if CsvRepository.__instance is None:
            CsvRepository.__instance = CsvRepository()
            try:
                with open(CsvRepository.csv_filename, mode="a", newline="") as file:
                    csv.writer(file)
            except Exception as e:
                print(f"An error occurred while creating the CSV: {str(e)}")
        return CsvRepository.__instance

    def task_exists(self, id: str) -> bool:
        tasks = self.read_tasks()
        for task in tasks:
            if task.id == id:
                return True
        return False

    def create_task(self, task: Task):
        try:
            with open(CsvRepository.csv_filename, mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(
                    [
                        task.id,
                        task.title,
                        task.description,
                        task.completed,
                        task.due_date,
                    ]
                )
            print(str(task))
        except Exception as e:
            print(f"An error occurred while saving the task to CSV: {str(e)}")

    def read_tasks(self) -> list[Task]:
        tasks: list[Task] = []
        with open(CsvRepository.csv_filename, mode="r") as file:
            reader = csv.DictReader(
                file,
                fieldnames=["id", "title", "description", "completed", "due_date"],
            )
            for row in reader:
                tasks.append(Task(**row))
        return tasks

    def update_task(self, task_to_update: Task):
        tasks = self.read_tasks()
        with open(CsvRepository.csv_filename, mode="w", newline="") as file:
            writer = csv.DictWriter(
                file, fieldnames=["id", "title", "description", "completed", "due_date"]
            )
            writer = csv.writer(file)
            for task in tasks:
                if task_to_update.id == task.id:
                    writer.writerow(
                        [
                            task_to_update.id,
                            task_to_update.title,
                            task_to_update.description,
                            task_to_update.completed,
                            task_to_update.due_date,
                        ]
                    )
                else:
                    writer.writerow(
                        [
                            task.id,
                            task.title,
                            task.description,
                            task.completed,
                            task.due_date,
                        ]
                    )

    def delete_task(self, id: str):
        # read each of the rows and map them to a Task object
        tasks: list[Task] = []
        with open(CsvRepository.csv_filename, mode="r") as file:
            # no header row
            reader = csv.DictReader(
                file, fieldnames=["id", "title", "description", "completed", "due_date"]
            )
            for row in reader:
                to_delete = Task(**row).id == id
                if to_delete is False:
                    tasks.append(Task(**row))
        # delete the task from the list
        with open(CsvRepository.csv_filename, mode="w", newline="") as file:
            writer = csv.DictWriter(
                file, fieldnames=["id", "title", "description", "completed", "due_date"]
            )
            writer = csv.writer(file)
            for task in tasks:
                writer.writerow(
                    [
                        task.id,
                        task.title,
                        task.description,
                        task.completed,
                        task.due_date,
                    ]
                )

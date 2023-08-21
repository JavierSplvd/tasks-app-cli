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
                    writer.writerow(task.to_dict())

    def delete_task(self, id: str):
        # O(n) time complexity
        output_file_path: str = CsvRepository.csv_filename + "_"
        with open(output_file_path, mode="w") as output_file:
            with open(CsvRepository.csv_filename, mode="r") as original_file:
                reader = csv.reader(original_file)
                for row in reader:
                    to_delete = row[0] == id
                    if to_delete is False:
                        # join list with commas and add newline
                        output_file.write(",".join(row) + "\n")
        os.remove(CsvRepository.csv_filename)
        os.rename(output_file_path, CsvRepository.csv_filename)

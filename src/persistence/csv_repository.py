import csv
from entities.task import Task


# This class uses the Singleton pattern.
class CsvRepository:
    __instance = None

    @staticmethod
    def get_instance():
        if CsvRepository.__instance is None:
            CsvRepository.__instance = CsvRepository()
        return CsvRepository.__instance

    def task_exists(self, id: str, csv_filename: str) -> bool:
        tasks = self.read_tasks(csv_filename)
        for task in tasks:
            if task.id == id:
                return True
        return False

    def read_tasks(self, csv_filename: str) -> list[Task]:
        tasks: list[Task] = []
        with open(csv_filename, mode="r") as file:
            reader = csv.DictReader(
                file,
                fieldnames=["id", "title", "description", "completed", "due_date"],
            )
            for row in reader:
                tasks.append(Task(**row))
        return tasks

    def update_task(self, task_to_update: Task, csv_filename: str):
        tasks = self.read_tasks(csv_filename)
        with open(csv_filename, mode="w", newline="") as file:
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

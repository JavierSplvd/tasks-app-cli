from entities.task import Task
from persistence.csv_repository import CsvRepository


def update_task(task: Task, csv_filename: str):
    if CsvRepository.get_instance().task_exists(task.id, csv_filename):
        CsvRepository.get_instance().update_task(task, csv_filename)
        print("Task updated!")
    else:
        print("Task not found!")

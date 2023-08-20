from entities.task import Task
from persistence.csv_repository import CsvRepository


def update_task(task: Task):
    if CsvRepository.get_instance().task_exists(task.id):
        CsvRepository.get_instance().update_task(task)
        print("Task updated!")
    else:
        print("Task not found!")

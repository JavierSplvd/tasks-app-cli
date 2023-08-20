from entities.task import Task
from persistence.csv_repository import CsvRepository


def create_task(task: Task):
    if CsvRepository.get_instance().task_exists(task.id):
        Exception("Task already exists!")
    CsvRepository.get_instance().create_task(task)

from entities.task import Task
from persistence.csv_repository import CsvRepository


def create_task(task: Task) -> Task:
    if CsvRepository.get_instance().task_exists(task.id):
        raise Exception("Task already exists!")
    return CsvRepository.get_instance().create_task(task)

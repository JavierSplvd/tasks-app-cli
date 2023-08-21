from entities.task import Task
from persistence.csv_repository import CsvRepository


def create_task(task: Task) -> Task:
    return CsvRepository.get_instance().create_task(task)

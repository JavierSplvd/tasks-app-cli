from entities.task import Task
from persistence.csv_repository import CsvRepository


def read_tasks() -> list[Task]:
    return CsvRepository.get_instance().read_tasks()

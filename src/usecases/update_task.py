from entities.task import Task
from persistence.csv_repository import CsvRepository


def update_task(task: Task) -> Task:
    if CsvRepository.get_instance().task_exists(task.id):
        CsvRepository.get_instance().update_task(task)
        return task
    else:
        raise Exception("Task does not exist!")
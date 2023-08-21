from persistence.csv_repository import CsvRepository


def delete_task(id: str) -> None:
    if CsvRepository.get_instance().task_exists(id):
        CsvRepository.get_instance().delete_task(id)
    else:
        raise Exception("Task does not exist!")

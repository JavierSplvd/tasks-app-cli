from persistence.csv_repository import CsvRepository


def delete_task(id: str) -> None:
    CsvRepository.get_instance().delete_task(id)

import csv
from entities.task import Task


def delete_task(id: str, csv_filename: str) -> None:
    # read each of the rows and map them to a Task object
    tasks: list[Task] = []
    with open(csv_filename, mode="r") as file:
        # no header row
        reader = csv.DictReader(file, fieldnames=["id", "title", "description", "completed", "due_date"])
        for row in reader:
            to_delete = Task(**row).id == id
            if to_delete is False:
                tasks.append(Task(**row))
    # delete the task from the list
    with open(csv_filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "title", "description", "completed", "due_date"])
        writer = csv.writer(file)
        for task in tasks:
            writer.writerow([task.id, task.title, task.description, task.completed, task.due_date])


            
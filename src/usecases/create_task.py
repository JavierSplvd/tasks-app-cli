import csv

from entities.task import Task


def create_task(task: Task, csv_filename: str):
    try:
        with open(csv_filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([task.title, task.description])
        print("Task created!")
        print(str(task))
    except Exception as e:
        print(f"An error occurred while saving the task to CSV: {str(e)}")

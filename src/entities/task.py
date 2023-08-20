import uuid


class Task:
    def __init__(
        self,
        id: str | None,
        title: str,
        description: str,
        completed: bool,
        due_date: str,
    ):
        self.id = id if id is not None else str(uuid.uuid4())
        self.title = title
        self.description = description
        self.completed = completed
        self.due_date = due_date

    def __str__(self):
        return f"| {self.id} | {trim_string(self.title, 12)} | {trim_string(self.description, 20)} | {'Completed' if self.completed else 'To do    '} | {self.due_date} |"

    def get_task_details(self):
        return {
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "due_date": self.due_date,
        }


def trim_string(input_string: str, max_length: int):
    if len(input_string) <= max_length:
        return input_string + " " * (max_length - len(input_string))
    else:
        return input_string[: max_length - 3] + "..."
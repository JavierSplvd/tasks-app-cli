import click

from entities.task import Task
from usecases.create_task import create_task
from usecases.delete_task import delete_task
from usecases.read_tasks import read_tasks
from usecases.update_task import update_task


@click.group()
def cli():
    """This CLI is a simple task manager. The items are stored in a CSV file on the HOME directory. A list of commands is available below.

    \b
    The task has the following attributes:
    \b
    - Id is a UUID that is automatically generated.
    \b
    - Title is a string.
    \b
    - Description is a string.
    \b
    - Completed is a boolean. It is represented as the string "Completed" or "To do".
    \b
    - Due date is a string in the format YYYY-MM-DD. The date is not validated.

    \b
    List tasks:
    task_manager.py ls

    \b
    Add task:
    task_manager.py add "title" "description" "1999-12-31"

    \b
    Update task:
    task_manager.py update "1ec475e3-9ee8-4e50-b7ae-45aeb624e1fd" "TTT" "DDD" "True" "1999-12-31"

    \b
    Delete task:
    task_manager.py delete "1ec475e3-9ee8-4e50-b7ae-45aeb624e1fd"
    """
    pass


@click.command()
def ls():
    """List tasks

    \b
    Example:
    task_manager.py ls
    """
    click.echo("List tasks")
    tasks = read_tasks()
    [click.echo(task) for task in tasks]


@cli.command()
@click.argument("title")
@click.argument("description")
@click.argument("due_date")
def add(title, description, due_date):
    """Add task

    \b
    The id is automatically generated.

    \b
    title: string
    description: string
    due_date: string

    \b
    Example:
    task_manager.py add "title" "description" "1999-12-31"
    """
    click.echo("Add task")
    task = create_task(Task(None, title, description, False, due_date))
    click.echo(task)


@cli.command()
@click.argument("id")
@click.argument("title")
@click.argument("description")
@click.argument("completed")
@click.argument("due_date")
def update(id, title, description, completed, due_date):
    """Update task

    \b
    id: string
    title: string
    description: string
    completed: string
    due_date: string

    \b
    Example:
    task_manager.py update "1ec475e3-9ee8-4e50-b7ae-45aeb624e1fd" "TTT" "DDD" "True" "1999-12-31"
    """
    click.echo("Update task")
    task = update_task(Task(id, title, description, completed, due_date))
    click.echo(task)


@cli.command()
@click.argument("id")
def delete(id):
    """Delete task

    \b
    id: string

    \b
    Example:
    task_manager.py delete "1ec475e3-9ee8-4e50-b7ae-45aeb624e1fd"
    """
    click.echo("Delete task")
    delete_task(id)


cli.add_command(ls)

if __name__ == "__main__":
    cli()

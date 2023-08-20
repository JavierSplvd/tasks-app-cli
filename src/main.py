import click

from entities.task import Task
from usecases.create_task import create_task
from usecases.delete_task import delete_task
from usecases.read_tasks import read_tasks
from usecases.update_task import update_task


@click.group()
def cli():
    pass


@click.command()
def ls():
    click.echo("List tasks")
    tasks = read_tasks()
    [click.echo(task) for task in tasks]


@cli.command()
@click.argument("title")
@click.argument("description")
@click.argument("due_date")
def add(title, description, due_date):
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
    click.echo("Update task")
    task = update_task(Task(id, title, description, completed, due_date))
    click.echo(task)

@cli.command()
@click.argument("id")
def delete(id):
    click.echo("Delete task")
    delete_task(id)


cli.add_command(ls)

if __name__ == "__main__":
    cli()

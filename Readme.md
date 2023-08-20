# Install development environment

Using Powershell:

'''
> .venv\scripts\activate
(venv) >
'''

# User stories

1. As a user I want to have a CLI to interact with the app.
2. As a user I want to create new tasks with some basic information.
3. As a user I want to read all the tasks on a tabular format to have an easy overview of the existing data.
4. As a user I want to update the task information to react to changes or fix errors.
5. As a user I want to delete the task in case it is no longer relevant.

# Run tests

'''
python -m unittest discover -s "./src" -t "./src"
'''
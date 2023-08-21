# Task Manager

This is my solution to the task manager CLI test case.

I have used the combination of python+click to create a simple CLI application. Python is a language that let you prototype fast, has a wide variety of packages and big community. Click is a module that let you create CLI applications with a few lines of code (check the task-manager.py file) as it has a good default configuration that you can override if needed.

I have separated the code in three folders:

1. Entities: This folder contains the classes that represent the data model of the application, in this simple case there are only tasks.
2. Persistence: This folder contains the classes that are responsible for the persistence of the data, following the repository pattern. For this simple case I have used a csv file to store the data.
3. Use cases: each of the functions defined represent a interaction between the user and the system to achieve a goal.

# Requirements

For this project I will use Windows OS and Powershell as the command line interface.

- Windows 10
- Powershell
- Python 3.11
- Visual Studio Code 1.80.1

# User stories

The Task Manager CLI helps the user in the following ways:

1. As a user I want to create new tasks with some basic information.
2. As a user I want to read all the tasks on a tabular format to have an easy overview of the existing data.
3. As a user I want to update the task information to react to changes or fix errors.
4. As a user I want to delete the task in case it is no longer relevant.

# Getting started

Using Powershell on the root folder install the dependencies and run the tests.

```
.venv\scripts\activate
python .\run_tests.py
python .\src\task-manager.py --help
```

# Future improvements

1. Repository Factory that serves different repositories implementations depending on the some configuration (for example csv, json, sql-lite, API rest).
2. Distribute the application as a package to be installed with pip.
3. CI pipeline to run tests and check coverage.
4. Input validation when creating and updating tasks.
5. makefile to install dependencies and run tests.

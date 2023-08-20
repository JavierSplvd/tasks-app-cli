import time
import unittest
import os

from entities.task import Task
from usecases.create_task import create_task
from usecases.create_database import create_database


class test_create_task(unittest.TestCase):
    def setUp(self):
        self.csv_filename = f"test_tasks_{int(time.time())}.csv"
        create_database(self.csv_filename)
        self.task_data: list[Task] = [
            Task(None, "Task 1", "Description 1", True, "2021-01-01"),
            Task(None, "Task 2", "Description 2", False, "2021-01-02"),
            Task(None, "Task 3", "Description 3", True, "2021-01-03"),
        ]

    def tearDown(self):
        if os.path.exists(self.csv_filename):
            os.remove(self.csv_filename)

    def test_save_task_to_csv(self):
        for task in self.task_data:
            create_task(task, self.csv_filename)

        self.assertTrue(os.path.exists(self.csv_filename))

        with open(self.csv_filename, mode="r") as file:
            lines = file.readlines()
            self.assertEqual(len(lines), len(self.task_data))
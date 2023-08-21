import os
import unittest

from entities.task import Task
from persistence.csv_repository import CsvRepository
from usecases.create_task import create_task


class test_create_task(unittest.TestCase):
    def setUp(self):
        self.task_data: list[Task] = [
            Task(None, "Task 1", "Description 1", True, "2021-01-01"),
            Task(None, "Task 2", "Description 2", False, "2021-01-02"),
            Task(None, "Task 3", "Description 3", True, "2021-01-03"),
        ]

    def setUpClass():
        if os.path.exists(CsvRepository.csv_filename):
            os.remove(CsvRepository.csv_filename)

    def tearDown(self):
        os.remove(CsvRepository.csv_filename)

    def test_save_task_success(self):
        for task in self.task_data:
            create_task(task)

        self.assertEqual(len(CsvRepository.get_instance().read_tasks()), 3)

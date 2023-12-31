import os
import unittest

from entities.task import Task
from persistence.csv_repository import CsvRepository
from usecases.read_tasks import read_tasks


class test_read_tasks(unittest.TestCase):
    def setUp(self):
        self.task_data: list[Task] = [
            Task("1", "Task 1", "Description 1", True, "2021-01-01"),
            Task(None, "Task 2", "Description 2", False, "2021-01-02"),
            Task(None, "Task 3", "Description 3", True, "2021-01-03"),
        ]
        for task in self.task_data:
            CsvRepository.get_instance().create_task(task)

    def setUpClass():
        if os.path.exists(CsvRepository.csv_filename):
            os.remove(CsvRepository.csv_filename)

    def tearDown(self):
        os.remove(CsvRepository.csv_filename)

    def test_read_tasks_from_csv(self):
        tasks = read_tasks()
        self.assertEqual(len(tasks), 3)

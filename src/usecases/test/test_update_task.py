import os
import unittest

from entities.task import Task
from persistence.csv_repository import CsvRepository
from usecases.update_task import update_task


class test_update_task(unittest.TestCase):
    def setUp(self):
        self.task_data: list[Task] = [
            Task("1", "Task 1", "Description 1", True, "2021-01-01"),
            Task(None, "Task 2", "Description 2", False, "2021-01-02"),
            Task(None, "Task 3", "Description 3", True, "2021-01-03"),
        ]
        for task in self.task_data:
            CsvRepository.get_instance().create_task(task)

    def tearDown(self):
        os.remove(CsvRepository.csv_filename)

    def test_update_task_from_csv(self):
        update_task(Task("1", "Task 100", "Description 100", False, "2030-01-01"))
        tasks = CsvRepository.get_instance().read_tasks()
        self.assertEqual(len(tasks), 3)
        self.assertEqual(tasks[0].id, "1")
        self.assertEqual(tasks[0].title, "Task 100")
        self.assertEqual(tasks[0].description, "Description 100")
        self.assertEqual(tasks[0].completed, False)
        self.assertEqual(tasks[0].due_date, "2030-01-01")

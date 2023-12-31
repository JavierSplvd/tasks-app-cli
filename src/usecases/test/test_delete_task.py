import os
import unittest

from entities.task import Task
from persistence.csv_repository import CsvRepository
from usecases.create_task import create_task
from usecases.delete_task import delete_task


class test_delete_task(unittest.TestCase):
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

    def test_delete_task_success(self):
        delete_task("1")
        self.assertEqual(len(CsvRepository.get_instance().read_tasks()), 2)

    def test_given_wrong_id_should_raise_exception(self):
        with self.assertRaises(Exception) as context:
            delete_task("wrong")
        self.assertTrue("Task does not exist!" in str(context.exception))

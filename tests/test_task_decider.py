import unittest
from src.task import Task
from src.task_decider import task_decider


class TestTaskDecider(unittest.TestCase):
    
    def setUp(self):
        self.dishes = Task("Wash Dishes", 10)
        self.dinner = Task("Cook Dinner", 40)
        self.windows = Task("Clean Windows", 60)

    def test_class_has_discription(self):
        self.assertEqual("Wash Dishes", self.dishes.description)
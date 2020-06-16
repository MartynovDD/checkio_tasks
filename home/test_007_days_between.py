import unittest
from home.task_007_days_between import days_between


class TestDaysBetween(unittest.TestCase):

    def test_days_difference(self):
        self.assertEqual(days_between((1982, 4, 19), (1982, 4, 22)), 3, "Case 1")

    def test_month_difference(self):
        self.assertEqual(days_between((2014, 1, 1), (2014, 8, 27)), 238, "Case 2")

    def test_reversed_args(self):
        self.assertEqual(days_between((2014, 8, 27), (2014, 1, 1)), 238, "Case 3")

    def test_list_arg(self):
        self.assertEqual(days_between([1982, 4, 19], [1982, 4, 22]), 3, "Case 4")

    def test_insuf_args(self):
        self.assertEqual(days_between((2001,), (2000,)), "insufficient arguments", "Case 5")


if __name__ == "__main__":
    unittest.main()

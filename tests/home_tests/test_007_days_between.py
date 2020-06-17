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

    def test_only_year(self):
        self.assertEqual(days_between((2001,), (2000,)), 366, "Case 5")

    def test_incorrect_argument(self):
        self.assertRaises(TypeError, days_between("", ""))

    def test_year_and_month(self):
        self.assertEqual(days_between((2020, 5), (2020, 6)), 31, "Case 7")

    def test_full_datetime(self):
        self.assertEqual(days_between((1991, 1, 1, 0, 0), (1992, 1, 1, 0, 0)), 365, "Case 8")


if __name__ == "__main__":
    unittest.main()

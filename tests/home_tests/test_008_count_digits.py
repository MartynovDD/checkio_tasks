import unittest
from home.task_008_count_digits import count_digits


class TestCountDigits(unittest.TestCase):

    def test_text_without_digits(self):
        self.assertEqual(count_digits("hi"), 0, "Case 1")

    def test_text_with_one_digit(self):
        self.assertEqual(count_digits("who is 1st here"), 1, "Case 2")

    def test_text_with_two_digits(self):
        self.assertEqual(count_digits("my number is 22"), 2, "Case 3")

    def test_multistring_text(self):
        self.assertEqual(count_digits("As of March 2018, SpaceX had over 100 launches on its manifest"
                                      " representing about $12 billion in contract revenue"), 9, "Case 4")

    def test_empty_text(self):
        self.assertEqual(count_digits(""), 0, "Case 5")

    def test_int_argument(self):
        self.assertEqual(count_digits(42), 2, "Case 6")


if __name__ == "__main__":
    unittest.main()

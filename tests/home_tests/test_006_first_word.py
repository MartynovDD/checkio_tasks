import unittest
from home.task_006_first_word import first_word


class TestFirstWord(unittest.TestCase):

    def test_two_words(self):
        self.assertEqual(first_word("Hello world"), "Hello", "Case 1")

    def test_spaced_words(self):
        self.assertEqual(first_word(" a word "), "a", "Case 2")

    def test_apostrophe(self):
        self.assertEqual(first_word("don't touch it"), "don't", "Case 3")

    def test_comma(self):
        self.assertEqual(first_word("greetings, friends"), "greetings", "Case 4")

    def test_dot(self):
        self.assertEqual(first_word("Hello.World"), "Hello", "Case 5")

    def test_one_word(self):
        self.assertEqual(first_word("hi"), "hi", "Case 6")

    def test_empty_text(self):
        self.assertEqual(first_word(""), "invalid value", "Case 7")

    def test_int(self):
        self.assertEqual(first_word(1), "invalid value", "Case 8")


if __name__ == "__main__":
    unittest.main()

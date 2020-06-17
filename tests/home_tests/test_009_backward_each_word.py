import unittest
from home.task_009_backward_each_word import word_reverse


class TestWordReverse(unittest.TestCase):

    def test_empty_text(self):
        self.assertEqual(word_reverse(""), "", "Empty string")

    def test_one_word(self):
        self.assertEqual(word_reverse("hello"), "olleh", "One word")

    def test_two_words(self):
        self.assertEqual(word_reverse("test string"), "tset gnirts", "Two words")

    def test_words_and_letters(self):
        self.assertEqual(word_reverse("abc abc a b c"), "cba cba a b c", "Words and letters")

    def test_word_between_numbers_text(self):
        self.assertEqual(word_reverse("123 demo 4"), "123 omed 4", "Word between numbers")

    def test_only_numbers_text(self):
        self.assertEqual(word_reverse("1337 696"), "1337 696", "Text contains only numbers")

    def test_word_with_symbols(self):
        self.assertEqual(word_reverse("&&*%test"), "&&*%test", "Symbols + word")

    def test_integer_input(self):
        self.assertEqual(word_reverse(343), "error", "Only strings are allowed")


if __name__ == "__main__":
    unittest.main()

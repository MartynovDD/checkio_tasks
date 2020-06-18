import unittest
from home.task_011_between_markers import between_markers


class TestBetweenMarkers(unittest.TestCase):

    def test_one_word(self):
        self.assertEqual(between_markers("What is >apple<", ">", "<"), "apple", "One word")

    def test_two_words(self):
        self.assertEqual(between_markers("<body<h1>Foo bar</h1></body>",
                                         "<h1>", "</h1>"), "Foo bar", "Two words")

    def test_only_ending_marker(self):
        self.assertEqual(between_markers("Spam> hi", "<", ">"), "Spam", "Only ending marker")

    def test_only_opening_marker(self):
        self.assertEqual(between_markers("Hello [b]world", "[b]", "[/b]"), "world", "Only opening marker")

    def test_wrong_direction(self):
        self.assertEqual(between_markers("print me", "[b]", "[/b]"), "print me", "No markers at all")

    def test_numbers_bracers(self):
        self.assertEqual(between_markers("(123)", "(", ")"), "123", "Numbers in bracers")

    def test_empty_string(self):
        self.assertEqual(between_markers("", "{", "}"), "", "Empty string")

    def test_incorrect_args(self):
        self.assertEqual(between_markers(123, 1, 3), "error", "Incorrect arguments")


if __name__ == "__main__":
    unittest.main()
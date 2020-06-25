"""
You are given a text, which contains different english letters and punctuation symbols.
You should find the most frequent letter in the text.
The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a".
Make sure you do not count punctuation symbols, digits and whitespaces, only letters.

If you have two or more letters with the same frequency, then return the letter which comes first in the latin alphabet.
For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".
https://py.most_wanted_letter.org/en/mission/most-wanted-letter/
"""
import collections


def most_wanted_letter(text: str) -> str:
    """
    Finds a letter with maximum occurencies in given text
    :param text:
    :return: str
    """
    letters = sorted([letter for letter in text.lower() if letter.isalpha()])
    return collections.Counter(letters).most_common()[0][0] if letters else ""


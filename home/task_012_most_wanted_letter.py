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


def most_wanted_letter(text: str) -> str:
    """
    Find and return letter with maximum occurencies in given text
    """
    text = str.lower(text)
    textnospace = text.replace(' ', '')
    itemcount = []
    for char in textnospace:
        if char.isalpha():
            itemcount.append((char, textnospace.count(char)))
            itemcount.sort(key=lambda x: (-x[1], x[0]))
    return itemcount[0][0]


if __name__ == "__main__":
    assert most_wanted_letter("Hello World!") == "l", "Hello test"
    assert most_wanted_letter("How do you do?") == "o", "O is most wanted"
    assert most_wanted_letter("One") == "e", "All letter only once."
    assert most_wanted_letter("Oops!") == "o", "Don't forget about lower case."
    assert most_wanted_letter("AAaooo!!!!") == "a", "Only letters."
    assert most_wanted_letter("abe") == "a", "The First."
    assert most_wanted_letter("a" * 9000 + "b" * 1000) == "a", "Long."
    assert most_wanted_letter("ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba") == "a"
    assert most_wanted_letter("i-d-d-q-d") == "d"
    assert most_wanted_letter("      d       ") == "d"
    assert most_wanted_letter("12345,12345,12345 S 12345,12345") == "s"

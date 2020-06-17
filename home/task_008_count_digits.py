"""
You need to count the number of digits in a given string.
https://py.checkio.org/en/mission/count-digits/
"""


def count_digits(text: str) -> int:
    """
    Counts digits in the given string
    """
    text = str(text)
    digits = [letter.isdigit() for letter in text]
    return sum(digits)


if __name__ == "__main__":
    assert count_digits("hi") == 0, "Case 1"
    assert count_digits("who is 1st here") == 1, "Case 2"
    assert count_digits("my number is 22") == 2, "Case 3"
    assert count_digits("As of March 2018, SpaceX had over 100 launches on its manifest"
                        " representing about $12 billion in contract revenue") == 9, "Case 4"
    assert count_digits('') == 0, "Case 5"
    assert count_digits(42) == 2, "Case 6"

# TODO : implement border case and incorrect case
# TODO : use unittest
# TODO: use list comprehension instead of current solution

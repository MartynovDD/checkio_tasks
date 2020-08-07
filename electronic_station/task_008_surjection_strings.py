"""
Maybe it's a cipher? Maybe, but we don’t know for sure.

Maybe you can call it "homomorphism"? i wish I know this word before.

You need to check that the 2 given strings are isometric.
This means that a character from one string can become a match for characters from another string.

One character from one string can correspond only to one character from another string.
Two or more characters of one string can correspond to one character of another string, but not vice versa.

Input: Two arguments. Both strings.
Output: Boolean.
both strings are the same size
"""
from utils.check_type import check_type


def are_isometric(first_string: str, second_string: str) -> bool:
    """
    Checks whether two given strings are isometric
    :param first_string: First string to compare
    :param second_string: Second string to compare
    :return: True if strings are isometric, False if strings are not isometric or have different lentgth
    """
    check_type(str, first_string)
    check_type(str, second_string)

    if len(first_string) != len(second_string):
        return False

    letters = [i for i, _ in set(zip(first_string, second_string))]
    return len(letters) == len(set(letters))

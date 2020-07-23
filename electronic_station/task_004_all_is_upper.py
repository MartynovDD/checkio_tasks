"""
Check if a given string has all symbols in upper case.
If the string is empty or doesn't have any letter in it - function should return False.

Input: A string.
Output: a boolean.
Precondition: a-z, A-Z, 1-9 and spaces
https://py.checkio.org/ru/mission/all-upper-ii/
"""
from utils.check_type import check_type


def is_all_upper(text: str) -> bool:
    """
    Checks if all characters in text are uppercase
    :param text: A string to analyse
    :return: True if all characters are uppercase, False otherwise
    """
    check_type(str, text)
    return text.isupper()

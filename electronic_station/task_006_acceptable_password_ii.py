"""
In this mission you need to create a password verification function.

Those are the verification conditions:

    the length should be bigger than 6;
    should contain at least one digit.

Input: A string.

Output: A bool.
https://py.checkio.org/ru/mission/acceptable-password-ii/
"""
from utils.check_type import check_type


def is_acceptable_password(password: str) -> bool:
    """
    Сhecks if given password length is >6 and it contains at least one digit
    :param password: Password string to analyze
    :return: True if password is acceptable, False otherwise
    """
    check_type(str, password)

    length_is_acceptable = False
    has_digit = False

    if len(password) > 6:
        length_is_acceptable = True

    for character in password:
        if character.isdigit():
            has_digit = True

    return length_is_acceptable and has_digit


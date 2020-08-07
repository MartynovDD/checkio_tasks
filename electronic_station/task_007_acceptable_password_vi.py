"""
In this mission you need to create a password verification function.

Those are the verification conditions:

    the length should be bigger than 6;
    should contain at least one digit, but it cannot consist of just digits;
    having numbers or containing just numbers does not apply to the password longer than 9.
    a string should not contain the word "password" in any case;
    should contain 3 different letters (or digits) even if it is longer than 10

Input: A string.
Output: A bool.
https://py.checkio.org/ru/mission/acceptable-password-vi/
"""
import string
from utils.check_type import check_type


def is_acceptable_password(password: str) -> bool:
    # TODO: Split into smaller funcs
    """
    Checks if given password string meets required conditions:
        - length > 6;
        - contains at least one digit, but cannot consist of just digits (except condition 3);
        - if password length > 9 then second condition is skipped;
        - should not contain the word "password" in any case;
        - should contain 3 different letters or digits regardless of length
    :param password: Password string to analyze
    :return: True if password is acceptable, False otherwise
    """
    check_type(str, password)

    blacklist_word = "password"
    if len(password) <= 6:
        return False
    if blacklist_word in password.lower():
        return False

    full_alphabet = string.ascii_lowercase + string.digits
    if len(set(password.lower()) & set(full_alphabet)) < 3:
        return False

    if len(password) > 9:
        return True

    if password.isdigit():
        return False

    if not set(string.digits) & set(password):
        return False

    return True

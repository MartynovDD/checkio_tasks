"""
Stephan and Sophia forget about security and use simple passwords for everything. Help Nikola develop a password
security check module. The password will be considered strong enough if its length is greater than or equal to 10
symbols, it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it. The
password contains only ASCII latin letters or digits.
https://py.checkio.org/mission/house-password/
"""
import string


def check_password(password):
    """
    Checks given password to meet required conditions (at least one digit, one uppercase letter and one lowercase letter
    If conditions are met function returns True
    Otherwise function returns False
    """
    password_set = set(password)
    # The password will be considered strong enough if its length is greater than or equal to 10
    # symbols
    length_flag = len(password) >= 10
    digits_flag = bool(password_set.intersection(set(string.digits)))
    uppercase_flag = bool(password_set.intersection(set(string.ascii_uppercase)))
    lowercase_flag = bool(password_set.intersection(set(string.ascii_lowercase)))
    return length_flag and digits_flag and uppercase_flag and lowercase_flag


if __name__ == "__main__":
    assert check_password("123456") == False  # Case 1
    assert check_password("qwerty") == False  # Case 2
    assert check_password("1erts4") == False  # Case 3
    assert check_password("ASDAFAFDS") == False  # Case 4
    assert check_password("AS214S34") == False  # Case 5
    assert check_password("a3fSgf4Df5") == True  # Case 6
    assert check_password("Aa1111111111")
    assert check_password("Aa1234567890")

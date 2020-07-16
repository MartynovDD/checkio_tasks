"""
You are given a positive integer.
Your function should calculate the product of the digits excluding any zeroes.

For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).
https://py.checkio.org/en/mission/digits-multiplication/
Input: A positive integer.

Output: The product of the digits as an integer.
Precondition: 0 < number < 1000000
"""
from utils.check_type import check_type


def multiply_digits(number: int) -> int:
    """
    Calculates the product of all digits in given number
    :param number: An int number
    :return: int product of digits in number, excluding zeroes
    """
    check_type(int, number)
    assert 0 < number < 1000000

    digits = [int(digit) for digit in str(number) if int(digit)]
    product = 1

    for digit in digits:
        product *= digit

    return product

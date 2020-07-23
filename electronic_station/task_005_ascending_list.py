"""
Determine whether the sequence of elements items is ascending so that its each element
is strictly larger than (and not merely equal to) the element that precedes it.

Input: Iterable with ints.
Output: Bool.
https://py.checkio.org/ru/mission/ascending-list/
"""
from typing import Iterable
from utils.check_type import check_type


def is_ascending(items: Iterable[int]) -> bool:
    """
    Checks if all items in given iterable are in ascending order
    :param items: An iterable of integers
    :return: True if items in ascending order, otherwise False
    """
    validate_iterable(items)

    ascending = True
    for index in range(len(items) - 1):
        if items[index] >= items[index + 1]:
            ascending = False

    return ascending


def validate_iterable(items: Iterable):
    """
    Validates iterable for is_ascending func
    :param items: Iterable of items
    :return: None if all items are valid, raises Assertion
    """
    if not isinstance(items, Iterable):
        raise TypeError("Given object is not Iterable")
    for item in items:
        check_type(int, item)

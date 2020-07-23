"""
Determine whether the sequence of elements items is ascending so that its each element
is strictly larger than (and not merely equal to) the element that precedes it.

Input: Iterable with ints.
Output: Bool.
https://py.checkio.org/ru/mission/ascending-list/
"""
from typing import Iterable


def is_ascending(items: Iterable[int]) -> bool:
    """
    Checks if all items in given iterable are in ascending order
    :param items:
    :return:
    """
    assert isinstance(items, Iterable)

    ascending = True
    for index in range(len(items) - 1):
        if items[index] >= items[index + 1]:
            ascending = False

    return ascending

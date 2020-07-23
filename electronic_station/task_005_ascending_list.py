"""
Determine whether the sequence of elements items is ascending so that its each element
is strictly larger than (and not merely equal to) the element that precedes it.

Input: Iterable with ints.
Output: Bool.
https://py.checkio.org/ru/mission/ascending-list/
"""
from typing import Iterable
from utils.check_type import check_type


def is_ascending(items: Iterable) -> bool:
    """

    :param items:
    :return:
    """
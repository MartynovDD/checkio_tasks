"""
Sort the given iterable so that its elements end up in the decreasing frequency order,
that is, the number of times they appear in elements.
If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.
"""
import typing
from collections import Counter


def frequency_sort(items: typing.Iterable) -> list:
    """
    Sorts iterable by item frequency
    :param items: Iterable to sort
    :return: list sorted by item frequency in given Iterable
    """
    counts = Counter(items).most_common()
    result = []
    for k, v in counts:
        for n in range(v):
            result.append(k)
    return result

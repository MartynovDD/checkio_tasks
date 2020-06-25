"""
Sort the given iterable so that its elements end up in the decreasing frequency order,
that is, the number of times they appear in elements.
If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.
"""
import typing
import collections
from utils.exception_catcher import exception_catcher


def frequency_sort(items: typing.Iterable) -> list:
    # TODO Fix to pass test 3
    # TODO Add pytest tests
    """
    Sorts iterable by item frequency
    :param items: Iterable
    :return: list
    """
    counts = collections.Counter(items)
    result = sorted(items, key=lambda x: (counts[x], x), reverse=True)
    return result


if __name__ == "__main__":
    assert frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert frequency_sort([17, 99, 42]) == [17, 99, 42]
    assert frequency_sort([]) == []
    assert frequency_sort([1]) == [1]
    assert frequency_sort(["", "", "a", "", ""]) == ["", "", "", "", "a"]
    assert frequency_sort("hello") == ["l", "l", "h", "e", "o"]
    assert exception_catcher(frequency_sort) == TypeError
    assert exception_catcher(frequency_sort, 4.4) == AttributeError

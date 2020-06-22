"""
You are given a non-empty list of integers (X).
For this task, you should return a list consisting of only the non-unique elements in this list.
To do so you will need to remove all unique elements (elements which are contained in a given list only once).
When solving this task, do not change the order of the list.
Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].
https://py.non_unique_elements.org/en/mission/non-unique-elements/
"""
import typing


def non_unique_elements(data: typing.Union[list, dict]) -> list:
    """

    :param data:
    :return:
    """
    if isinstance(data, dict):
        data = list(data.values())
    result_list = [item for item in data if data.count(item) > 1]
    return result_list



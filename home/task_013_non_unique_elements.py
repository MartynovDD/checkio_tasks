"""
You are given a non-empty list of integers (X).
For this task, you should return a list consisting of only the non-unique elements in this list.
To do so you will need to remove all unique elements (elements which are contained in a given list only once).
When solving this task, do not change the order of the list.
Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].
https://py.non_unique_elements.org/en/mission/non-unique-elements/
"""


def non_unique_elements(elements: list) -> list:
    """
    Delete all unique elements from list and return list
    """
    result_list = [item for item in elements if elements.count(item) > 1]
    return result_list


if __name__ == "__main__":
    assert non_unique_elements([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert non_unique_elements([1, 2, 3, 4, 5]) == [], "2nd example"
    assert non_unique_elements([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert non_unique_elements([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"
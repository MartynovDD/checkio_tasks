"""
You are given an array of integers.
You should find the sum of the integers with even indexes (0th, 2nd, 4th...).
Then multiply this summed number and the final element of the array together.
Don't forget that the first element has an index of 0.
For an empty array, the result will always be 0 (zero).
https://py.checkio.org/en/mission/even-last/
"""


def even_the_last(array):
    """
    Calculates the sum of integers on even positions in array
    then multiplies them by integer on last position in array
    """
    result = 0
    for i in range(0, len(array), 2):
        result = result + array[i]

    if array:
        result *= array[-1]
        return result
    else:
        return 0


if __name__ == "__main__":
    assert even_the_last([]) == 0, "Case 1"
    assert even_the_last([0, 1, 2, 3, 4, 5]) == 30, "Case 2"
    assert even_the_last([1, 4, 8]) == 72, "Case 3"
    assert even_the_last([10]) == 100, "Case 4"
    assert even_the_last([72, -19, -73, -59, 83, -79, -90]) == 720, "Case 5"

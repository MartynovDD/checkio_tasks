"""
How old are you in a number of days? It's easy to calculate - just subtract your birthday from today.
We could make this a real challenge though and count the difference between any dates.

You are given two dates as an array with three numbers - a year, month and day.
For example: 19 April 1982 will be (1982, 4, 19).
You should find the difference in days between the given dates. For example between today and tomorrow = 1 day.
The difference will always be either a positive number or zero, so don't forget about the absolute value.
https://py.checkio.org/ru/mission/days-diff/
"""
import datetime
import typing


def fill_date(date: typing.Iterable) -> tuple:
    date = list(date) + list((1 for _ in range(3 - len(date)))) + list((0 for _ in range(2)))
    return tuple(date)


def days_between(first_date: typing.Iterable, second_date: typing.Iterable) -> int:
    """
    Returns difference between date a and date b
    """
    try:
        difference = datetime.datetime(*fill_date(first_date)) - datetime.datetime(*fill_date(second_date))
        return abs(difference.days)
    except Exception as e:
        raise e


if __name__ == "__main__":
    assert days_between((1982, 4, 19), (1982, 4, 22)) == 3, "Case 1"
    assert days_between((2014, 1, 1), (2014, 8, 27)) == 238, "Case 2"
    assert days_between((2014, 8, 27), (2014, 1, 1)) == 238, "Case 3"
    assert days_between([1982, 4, 19], [1982, 4, 22]) == 3, "Case 4"
    assert days_between((2001,), (2000,)) == 366, "Case 5"
    assert days_between("", "") == 0, "Case 6"
    assert days_between((2020, 5), (2020, 6)) == 31, "Case 7"
    assert days_between((1991, 1, 1, 0, 0), (1992, 1, 1, 0, 0)) == 365, "Case 8"



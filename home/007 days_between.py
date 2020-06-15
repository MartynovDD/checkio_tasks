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


def days_between(a, b):
    """
    Returns difference between date a and date b
    """
    difference = datetime.date(*a) - datetime.date(*b)
    return abs(difference.days)


assert days_between((1982, 4, 19), (1982, 4, 22)) == 3, "Case 1"
assert days_between((2014, 1, 1), (2014, 8, 27)) == 238, "Case 2"
assert days_between((2014, 8, 27), (2014, 1, 1)) == 238, "Case 3"
assert days_between([1982, 4, 19], [1982, 4, 22]) == 3, "Case 4"

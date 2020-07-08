"""
Computer date and time format consists only of numbers, for example: 21.05.2018 16:30
Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes
Your task is simple - convert the input date and time from computer format into a "human" format.
https://py.checkio.org/en/mission/date-and-time-converter/
"""


def date_time(time: str) -> str:
    """
    Converts a datetime string to human readable format
    :param time: String containing date and time to process
    :return: Datetime string in human readable format (ex: 1 January 2000 year 0 hours 0 minutes)
    """
    return time
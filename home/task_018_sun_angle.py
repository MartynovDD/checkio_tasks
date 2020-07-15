"""
Your task is to find the angle of the sun above the horizon knowing the time of the day.
Input data: the sun rises in the East at 6:00 AM, which corresponds to the angle of 0 degrees.
At 12:00 PM the sun reaches its zenith, which means that the angle equals 90 degrees.
6:00 PM is the time of the sunset so the angle is 180 degrees.
If the input will be the time of the night (before 6:00 AM or after 6:00 PM),
your function should return - "I don't see the sun!".
https://py.checkio.org/en/mission/sun-angle/
"""
import typing
import re
from utils.check_type import check_type


def sun_angle(time: str) -> typing.Union[int, float, str]:
    """
    Calculates the sun angle using a time string
    :param time: a string of time in format HH:MM (ex: 12:00)
    :return: Sun angle if time of the day, otherwise "I don't see the sun!"
    """
    check_type(str, time)
    check_time_format(time)

    hour, minute = list(map(int, time.split(':')))
    check_time_values(hour, minute)

    angle_of_the_sun = 15 * hour + minute / 4 - 90
    return angle_of_the_sun if 0 <= angle_of_the_sun <= 180 else "I don't see the sun!"


def check_time_format(time: str) -> str:
    """
    Checks if provided string matches format HH:MM (H - hours, M - minutes)
    :param time: A string of time (ex. 06:00)
    :return: "ok!" if time string matches format, otherwise raise ValueError
    """
    pattern = re.compile(r"^(\d{2})(:)(\d{2})$")
    if not re.match(pattern, time):
        raise ValueError("Time string format is incorrect")
    return "ok!"


def check_time_values(hour: int, minute: int) -> str:
    """
    Validates the values of hour and minute
    :param hour: hour value
    :param minute: minute value
    :return: "ok!" if hour and minute are valid (0 <= hour <= 24, 0 <= minute <= 60),
            otherwise raises ValueError
    """
    if not 0 <= hour <= 24:
        raise ValueError("Hour value is incorrect")
    if not 0 <= minute <= 60:
        raise ValueError("Minute value is incorrect")
    return "ok!"

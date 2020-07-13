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
from utils.type_checker import type_checker


def sun_angle(time: str) -> typing.Union[int, float, str]:
    """
    Calculates the sun angle using a time string
    :param time: a string of time in format HH:MM (ex: 12:00)
    :return: Sun angle if time of the day, otherwise "I don't see the sun!"
    """
    type_checker(str, time)
    hour, minute = list(map(int, time.split(':')))
    angle = 15 * hour + minute / 4 - 90
    return angle if 0 <= angle <= 180 else "I don't see the sun!"

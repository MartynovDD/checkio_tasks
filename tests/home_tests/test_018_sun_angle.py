import pytest
from home.task_018_sun_angle import sun_angle


def test_seven_am():
    assert sun_angle("07:00") == 15, "07:00"


def test_one_pm():
    assert sun_angle("01:00") == "I don't see the sun!", "01:00"


def test_six_pm():
    assert sun_angle("18:00") == 180, "18:00"


def test_six_one_pm():
    assert sun_angle("18:01") == "I don't see the sun!", "18:01"


def test_six_am():
    assert sun_angle("06:00") == 0, "06:00"


def test_twelve_fifteen_am():
    assert sun_angle("12:15") == 93.75, "12:15"


def test_empty_string():
    with pytest.raises(ValueError):
        sun_angle("")


def test_no_args():
    with pytest.raises(TypeError):
        sun_angle()


def test_incorrect_args():
    with pytest.raises(TypeError):
        sun_angle(1245)

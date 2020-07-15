import pytest
from home.task_018_sun_angle import sun_angle, check_time_values
from hypothesis import given, assume
import hypothesis.strategies as st


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


@given(h=st.integers(min_value=0, max_value=24), m=st.integers(min_value=0, max_value=60))
def test_positive_time_values(h, m):
    assert check_time_values(h, m) == "ok!"


@given(h=st.floats(min_value=-999, max_value=999), m=st.floats(min_value=-999, max_value=999))
def test_negative_time_values(h, m):
    assume(not 0 <= h <= 24)
    assume(not 0 <= m <= 60)
    with pytest.raises(ValueError):
        check_time_values(h, m)


def test_incorrect_time_format():
    with pytest.raises(ValueError):
        sun_angle("0_6:00")


def test_no_args():
    with pytest.raises(TypeError):
        sun_angle()


def test_incorrect_args():
    with pytest.raises(TypeError):
        sun_angle(1245)

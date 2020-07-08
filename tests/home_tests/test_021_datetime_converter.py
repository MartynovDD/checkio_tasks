import pytest
from home.task_021_datetime_converter import date_time


def test_millenium():
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"


def test_birthday():
    assert date_time("06.06.1993 02:01") == "6 June 1993 year 2 hours 1 minute", "Birthday"


def test_no_args():
    with pytest.raises(TypeError):
        date_time()


def test_incorrect_args():
    with pytest.raises(TypeError):
        date_time(12345)

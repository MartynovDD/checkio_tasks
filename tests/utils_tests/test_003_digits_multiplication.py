import pytest
from electronic_station.task_003_digits_multiplication import multiply_digits


def test_one_two_three():
    assert multiply_digits(123450) == 120, "123450"


def test_thousand():
    assert multiply_digits(1000) == 1, "One thousand"


def test_four_ones():
    assert multiply_digits(1111) == 1, "1111"


def test_one():
    assert multiply_digits(1) == 1, "One"


def test_six_nines():
    assert multiply_digits(999999) == 531441, "999999"


def test_zero():
    with pytest.raises(AssertionError):
        multiply_digits(0)


def test_million():
    with pytest.raises(AssertionError):
        multiply_digits(1000000)


def test_no_args():
    with pytest.raises(TypeError):
        multiply_digits()


def test_incorrect_args():
    with pytest.raises(TypeError):
        multiply_digits("beep")

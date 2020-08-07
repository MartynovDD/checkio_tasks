import pytest
import string
from electronic_station.task_007_acceptable_password_vi import is_acceptable_password
from hypothesis import given, settings, Verbosity, strategies as st
from utils.generate_string import generate_string_from_groups


@given(password=st.text(alphabet=st.characters(whitelist_categories=("Ll",)), max_size=6))
@settings(verbosity=Verbosity.verbose)
def test_short_password(password):
    assert not is_acceptable_password(password), "Short password of letters"


@given(password=st.builds(generate_string_from_groups,
                          st.text(st.characters(whitelist_categories=("Ll",))),
                          st.integers(),
                          length=st.integers(max_value=6)))
@settings(verbosity=Verbosity.verbose)
def test_short_password_with_numbers(password):
    assert not is_acceptable_password(password), "Short password of letters and digits"


@given(password_set=st.sets(st.sampled_from(string.digits), min_size=10))
@settings(verbosity=Verbosity.verbose)
def test_long_digit_password(password_set):
    password = "".join(password_set)
    assert is_acceptable_password(password), "Long digit password"


@given(password_set=st.sets(st.sampled_from(string.ascii_letters), min_size=10))
@settings(verbosity=Verbosity.verbose)
def test_long_letter_password(password_set):
    password = "".join(password_set)
    assert is_acceptable_password(password), "Long letter password"


@given(password_set=st.sets(st.sampled_from(string.ascii_letters + string.digits), min_size=7, max_size=9))
@settings(verbosity=Verbosity.verbose)
def test_acceptable_password(password_set):
    password = "".join(password_set)
    assert is_acceptable_password(password), "Acceptable password"


def test_no_args():
    with pytest.raises(TypeError):
        is_acceptable_password()


@given(invalid_arg=st.one_of(st.integers(), st.floats(), st.binary()))
@settings(verbosity=Verbosity.verbose)
def test_incorrect_args(invalid_arg):
    with pytest.raises(TypeError):
        is_acceptable_password(invalid_arg)

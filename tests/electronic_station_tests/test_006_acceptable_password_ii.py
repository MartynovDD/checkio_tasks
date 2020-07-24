import pytest
from electronic_station.task_006_acceptable_password_ii import is_acceptable_password
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


@given(password=st.builds(generate_string_from_groups,
                          st.text(st.characters(whitelist_categories=("Ll",))),
                          st.integers(),
                          length=st.integers(min_value=7, max_value=30)))
@settings(verbosity=Verbosity.verbose)
def test_acceptable_password(password):
    assert is_acceptable_password(password), "Acceptable password (has length > 6, letters and digits)"


def test_no_args():
    with pytest.raises(TypeError):
        is_acceptable_password()


@given(invalid_arg=st.one_of(st.integers(), st.floats(), st.binary()))
@settings(verbosity=Verbosity.verbose)
def test_incorrect_args(invalid_arg):
    with pytest.raises(TypeError):
        is_acceptable_password(invalid_arg)



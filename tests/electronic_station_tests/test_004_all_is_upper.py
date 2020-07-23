import pytest
from electronic_station.task_004_all_is_upper import is_all_upper
from hypothesis import given, Verbosity, settings, strategies as st


@given(text=st.text(alphabet=st.characters(whitelist_categories=("Lu",)), min_size=2))
@settings(verbosity=Verbosity.verbose)
def test_all_upper(text):
    assert is_all_upper(text), "All is upper"


@given(text=st.text(alphabet=st.characters(whitelist_categories=("Ll", "Zs")), min_size=2))
@settings(verbosity=Verbosity.verbose)
def test_all_lower(text):
    assert not is_all_upper(text), "All is lower"


@given(text=st.text(alphabet=st.characters(whitelist_categories=("Nd", "Zs")), min_size=2))
@settings(verbosity=Verbosity.verbose)
def test_numbers(text):
    assert not is_all_upper(text), "Numbers"


@given(first_group=st.text(alphabet=st.characters(whitelist_categories=("Ll", "Zs")), min_size=2),
       second_group=st.text(alphabet=st.characters(whitelist_categories=("Lu", "Zs")), min_size=1),
       third_group=st.text(alphabet=st.characters(whitelist_categories=("Ll",)), min_size=1))
@settings(verbosity=Verbosity.verbose)
def test_mixed_cases(first_group, second_group, third_group):
    text = first_group + second_group + third_group
    assert not is_all_upper(text), "Mixed cases"


@given(first_group=st.text(alphabet=st.characters(whitelist_categories=("Lu",)), min_size=1),
       second_group=st.text(alphabet=st.characters(whitelist_categories=("Nd",)), min_size=1))
@settings(verbosity=Verbosity.verbose)
def test_uppercase_and_digits(first_group, second_group):
    text = first_group + second_group
    assert is_all_upper(text), "Uppercase characters and digits"


def test_empty_string():
    assert not is_all_upper(""), "Empty string"


def test_no_args():
    with pytest.raises(TypeError):
        is_all_upper()


@given(sample=st.one_of(st.floats(), st.binary(), st.integers(), st.booleans()))
@settings(verbosity=Verbosity.verbose)
def test_incorrect_args(sample):
    with pytest.raises(TypeError):
        is_all_upper(sample)

import pytest
from home.task_022_morse_decoder import morse_decoder


def test_hello_world():
    assert morse_decoder(".... . .-.. .-.. ---   .-- --- .-. .-.. -..") == "Hello world", "Two words"


def test_numbers():
    assert morse_decoder(".---- ----. ---.. ....-") == "1984", "Numbers"


def test_words_and_numbers():
    assert morse_decoder("-... .-.. .- -.. . .-. ..- -. -. . .-. ..--- ----- ....- ----.") == "Bladerunner2049", \
        "Words and numbers"


def test_empty_string():
    assert morse_decoder("") == "", "Empty string"


def test_no_arguments():
    with pytest.raises(TypeError):
        morse_decoder()


def test_incorrect_arguments():
    with pytest.raises(TypeError):
        morse_decoder(12345)

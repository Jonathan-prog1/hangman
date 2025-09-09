from helper import check_input_number, check_input_word
import pytest

def test_check_input_number():
    assert check_input_number("5") == 0
    with pytest.raises(ValueError, match="Please Enter a number"):
        check_input_number("hi")
        check_input_number(5)

def test_check_input_word():
    assert check_input_word("a") == 0
    with pytest.raises(ValueError, match="Please Enter a letter a-z"):
        check_input_word(1)
        check_input_word("1")


from plates import is_valid
import pytest

def test_invalid_length():
    assert is_valid("A") == False
    assert is_valid("5") == False
    assert is_valid("AAA222A") == False

def test_valid_length():
    assert is_valid("AA") == True

def test_invalid_number():
    assert is_valid("AA0A") == False
    assert is_valid("00AA") == False

def test_invalid_punctuation():
    assert is_valid("AA.222") == False
    assert is_valid("AA 00") == False
from bank import value
import pytest

def test_hello():
    assert value("hello there") == 0

def test_h():
    assert value("hey") == 20

def test_no_h():
    assert value("what's up") == 100
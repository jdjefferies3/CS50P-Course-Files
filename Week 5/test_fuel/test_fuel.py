from fuel import convert, gauge
import pytest

def test_convert_divide_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert_alpha():
    with pytest.raises(ValueError):
        convert("c/1")

def test_convert_x_over_y():
    with pytest.raises(ValueError):
        convert("4/3")

def test_gauge_empty():
    assert gauge(1) == "E"
    assert gauge(0) == "E"

def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
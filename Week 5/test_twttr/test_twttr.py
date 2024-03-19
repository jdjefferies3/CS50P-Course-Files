from twttr import shorten
import pytest

def test_shorten():
    assert shorten("Twitter") == "Twttr"
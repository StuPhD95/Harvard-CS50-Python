from fuel import convert
from fuel import gauge
import pytest

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("0/4") == 0

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"

def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_ValueError():
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ValueError):
        convert("-1/4")
    with pytest.raises(ValueError):
        convert("1.5/4")

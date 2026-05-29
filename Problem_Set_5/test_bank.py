from bank import value
import pytest

def test_hello():
    assert value("hello") == 0
    assert value("hello mate") == 0

def test_capital_hello():
    assert value("HELLO") == 0
    assert value("HELLO MATE") == 0

def test_first_letter():
    assert value("hi") == 20

def test_other_greeting():
    assert value("wassup") == 100

def test_number():
    assert value("1") == 100

from plates import is_valid
import pytest

def test_first_req():
    assert is_valid("123") == False
    assert is_valid("a123") == False

def test_second_req():
    assert is_valid("a") == False
    assert is_valid("HELLO123") == False

def test_third_req():
    assert is_valid("AAA222") == True
    assert is_valid("AAA022") == False
    assert is_valid("AAA22A") == False

def test_fourth_req():
    assert is_valid("AAA 22") == False
    assert is_valid("AAA.22") == False
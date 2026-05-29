from twttr import shorten
import pytest

# Note: pytest will only run functions that start with test_

def test_lower_case():
    assert shorten("stuart") == "strt"
    assert shorten("katie") == "kt"

def test_upper_case():
    assert shorten("STUART") == "STRT"
    assert shorten("KATIE") == "KT"

def test_numbers():
    assert shorten("CS50") == "CS50"

def test_punctuation():
    assert shorten("Hello, stuart!") == "Hll, strt!"
    assert shorten("What's up?") == "Wht's p?"

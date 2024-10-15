from fuel import convert, gauge
import pytest


def test_not_characters_variables1():
    with pytest.raises(ValueError):
        convert("cat/dog")


def test_not_characters_variables2():
    with pytest.raises(ValueError):
        convert("1/dog")

def test_not_characters_variables3():
    with pytest.raises(ValueError):
        convert("3/1")

def test_not_divided_by_0():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(10) == "10%"
    assert gauge(101) == "F"
    assert gauge(99) == "F"

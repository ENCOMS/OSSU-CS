import pytest
import datetime
from seasons import Time_born


def main():
    test_get_valid_date()
    test_get_invalid_date()
    test_valid_sing()
    test_get_no_date()


def test_get_valid_date(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "1990-04-15")

    born_date = Time_born.get_date()

    assert isinstance(born_date, datetime.date)
    assert born_date.year == 1990
    assert born_date.month == 4
    assert born_date.day == 15


def test_get_invalid_date(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "January 1, 1999")

    with pytest.raises(SystemExit) as e1:
        Time_born.get_date()

    assert e1.type == SystemExit
    assert str(e1.value) == "Invalid inputs"


def test_get_no_date(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "")

    with pytest.raises(SystemExit) as e2:
        Time_born.get_date()

    assert e2.type == SystemExit
    assert str(e2.value) == "Invalid inputs"


def test_valid_sing(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "1999-01-01")

    born_date = Time_born.get_date()
    minutes = Time_born.min_since(born_date, fixed_date="2000-01-01")

    assert minutes.sing() == "Five hundred twenty-five thousand, six hundred minutes"


if __name__ == "__main__":
    main()

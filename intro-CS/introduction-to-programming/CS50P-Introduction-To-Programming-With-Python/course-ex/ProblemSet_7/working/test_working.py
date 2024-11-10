from working import convert
import pytest


def main():
    test_am_pm()
    test_pm_am()
    test_raise_error()


def test_am_pm():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:30 AM to 5:30 PM") == "09:30 to 17:30"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_pm_am():
    assert convert("9:00 PM to 9:00 AM") == "21:00 to 09:00"
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"
    assert convert("5 PM to 9 AM") == "17:00 to 09:00"


def test_raise_error():
    with pytest.raises(ValueError):
        assert convert("9:00 PM - 9:00 AM") == ValueError
    with pytest.raises(ValueError):
        assert convert("9:60 PM - 9:00 AM") == ValueError
    with pytest.raises(ValueError):
        assert convert("9:00 PM - 9:60 AM") == ValueError
    with pytest.raises(ValueError):
        assert convert("8:60 AM to 4:60 PM") == ValueError
    with pytest.raises(ValueError):
        assert convert("9:00 to 17:00") == ValueError
    with pytest.raises(ValueError):
        assert convert("17:00 to 09:00") == ValueError
    with pytest.raises(ValueError):
        assert convert("9AM to 5PM") == ValueError


if __name__ == "__main__":
    main()

from response import is_valid
import pytest


def main():
    test_valid_email()
    test_invalid_email()
    test_text()


def test_valid_email():
    assert is_valid("gsssre183@gmail.com") == "Valid"
    assert is_valid("mallan@harvard.edu") == "Valid"
    assert is_valid("gsssre183@outlook.com") == "Valid"


def test_invalid_email():
    assert is_valid("malan@@@harvard.edu") == "Invalid"
    assert is_valid("gsssre183@gmail.com.") == "Invalid"
    assert is_valid("gsssre183@gmail") == "Invalid"
    assert is_valid("gsssre183@@@@") == "Invalid"
    assert is_valid("@gmail.com") == "Invalid"
    assert is_valid("this-is-an-invalid-email") == "Invalid"

def test_text():
    assert is_valid("this is the email assd@gmail.com") == "Invalid"
    assert is_valid("in harvard some davidm@harvard.edu") == "Invalid"


if __name__ == "__main__":
    main()

from numb3rs import validate
import pytest


def main():
    test_ip()
    test_no_ip()
    test_incomplete_ip()


def test_ip():
    assert validate("0.0.0.0") == True
    assert validate("1.2.3.4") == True
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.0") == True
    assert validate("275.3.6.28") == False
    assert validate("26.300.50.28") == False
    assert validate("140.247.280.144") == False
    assert validate("140.275.140.300") == False


def test_no_ip():
    assert validate("cat") == False
    assert validate("Dog.cat") == False
    assert validate("275.3.cat.dog") == False
    assert validate("My name is 255.255.255.0") == False


def test_incomplete_ip():
    assert validate("255") == False
    assert validate("300") == False
    assert validate("255.255..") == False
    assert validate("....") == False
    assert validate("..255.255") == False


if __name__ == "__main__":
    main()

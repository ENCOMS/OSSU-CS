import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    with pytest.raises(ValueError) as e:
        jar.capacity = 0
    assert e.type == ValueError
    with pytest.raises(ValueError) as e:
        jar.size = -1
    assert e.type == ValueError


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(5)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(5)
    assert jar.size == 10
    with pytest.raises(ValueError) as e:
        jar.deposit(5)
    assert e.type == ValueError
    with pytest.raises(ValueError) as e:
        jar.deposit(3)
    assert e.type == ValueError

def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    assert jar.size == 12
    jar.withdraw(5)
    assert jar.size == 7
    jar.withdraw(2)
    assert jar.size == 5
    with pytest.raises(ValueError) as e:
        jar.withdraw(6)
    assert e.type == ValueError
    with pytest.raises(ValueError) as e:
        jar.withdraw(12)
    assert e.type == ValueError

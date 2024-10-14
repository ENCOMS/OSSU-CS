from bank import value


def test_contains_hello():
    assert value("hello") == 0


def test_contains_Hello():
    assert value("Hello") == 0


def test_start_with_h():
    assert value("hi") == 20


def test_start_with_H():
    assert value("Hi") == 20


def test_not_hello():
    assert value("welcome") == 100


def test_not_Hello():
    assert value("Welcome") == 100
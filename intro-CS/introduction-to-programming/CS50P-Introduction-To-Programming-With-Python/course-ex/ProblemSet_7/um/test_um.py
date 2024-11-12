import pytest
from um import count


def main():
    test_um()
    test_puntuation()
    test_spaces()
    test_words()


def test_um():
    assert count("um") == 1
    assert count("uM") == 1
    assert count("Um") == 1
    assert count("UM") == 1


def test_puntuation():
    assert count("um?") == 1
    assert count("um,") == 1
    assert count("um.") == 1
    assert count("Um?") == 1
    assert count("Um,") == 1
    assert count("Um.") == 1
    assert count("uM?") == 1
    assert count("uM,") == 1
    assert count("uM.") == 1


def test_spaces():
    assert count(" um") == 1
    assert count(" um ") == 1
    assert count("um ") == 1
    assert count(" um, ") == 1
    assert count(" um,") == 1
    assert count(" Um,") == 1
    assert count(" um.") == 1
    assert count(" um,,,") == 1
    assert count(" um...") == 1


def test_words():
    assert count("yum") == 0
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("umbrella") == 0
    assert count("instrumentation") == 0
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    assert (
        count(
            "Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?"
        )
        == 2
    )
    assert count("Um, hello, um, world") == 2


if __name__ == "__main__":
    main()

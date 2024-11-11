import pytest
from um import count


def main():
    test_text()
    test_putuation_space()
    test_words()


def test_text():
    assert count("um") == "1"
    assert count("uM") == "1"
    assert count("Um") == "1"
    assert count("UM") == "1"


def test_putuation_space():
    assert count(" um") == "0"
    assert count(" um ") == "0"
    assert count("um?") == "1"
    assert count(" um, ") == "1"
    assert count(" um,") == "1"
    assert count("um,") == "1"
    assert count("um?") == "1"
    assert count(" um,,,") == "1"
    assert count(" um.") == "1"
    assert count("um.") == "1"
    assert count(" um...") == "1"


def test_words():
    assert count("yum") == "0"
    assert count("yummy") == "0"
    assert (
        count("instrumentation cryptosporidium instrumentalist instrumentality") == "0"
    )
    assert count("Um, thanks for the album.") == "1"
    assert count("Um, thanks, um...") == "2"
    assert (
        count(
            "Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?"
        )
        == "2"
    )
    assert count("um, hello, um, world") == "2"


if __name__ == "__main__":
    main()

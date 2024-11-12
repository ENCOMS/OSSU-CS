import pytest
from um import count


def main():
    test_normal()
    test_interrogation()
    test_words_with_um()
    test_many_words()
    test_different_puntuation()
    test_matching_words()


def test_normal():
    assert count("um") == 1
    assert count("UM") == 1
    assert count("Um... what are regular expressions?") == 1

def test_interrogation():
    assert count("um?") == 1

def test_words_with_um():
    assert count("Um, thanks for the album.") == 1

def test_many_words():
    assert count("Um, thanks, um, regular expressions make sense now.") == 2
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2
    assert count("album") == 0

def test_different_puntuation():
    assert count("Um, thanks, um...") == 2

def test_matching_words():
    assert count("Um? umbert, you did the wrong thing.") == 1


if __name__ == "__main__":
    main()


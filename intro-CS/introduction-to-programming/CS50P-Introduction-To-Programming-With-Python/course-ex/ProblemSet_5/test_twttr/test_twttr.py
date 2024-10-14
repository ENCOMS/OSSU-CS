'''
In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below,
wherein shorten expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted,
whether inputted in uppercase or lowercase

Then, in a file called test_twttr.py, implement one or more functions that collectively test your implementation of shorten thoroughly,
each of whose names should begin with test_ so that you can execute your tests with:

pytest test_twttr.py


the test should test for this or more:

- without vowel
- capitalized vowel
- without lowercase vowel
- omitting numbers
- printing in uppercase
- omitting punctuation
'''

from twttr import shorten


def test_without_vowel():
    assert shorten("rtgc") == "rtgc"


def test_capitalized_vowel():
    assert shorten("rAtgc") == "rtgc"


def test_without_lowercase_vowel():
    assert shorten("ratgc") == "rtgc"


def test_omitting_numbers():
    assert shorten("rAtgc123") == "rtgc123"


def test_printing_in_uppercase():
    assert shorten("RATGC") == "RTGC"


def test_omitting_punctuation():
    assert shorten("rAtgc...") == "rtgc..."

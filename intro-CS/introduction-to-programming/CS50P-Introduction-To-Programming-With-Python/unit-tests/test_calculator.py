from calculator import square
import pytest


# ex-2 simple test
'''
def main():
    test_square()


def test_square():
    if square(2) != 4:
        print("2 squared was not 4") #this create a possible corner case if not correctly implemented the square function, ex if used n + n instead of n * n.
    if square(3) != 9:
        print("3 squared was not 9")

if __name__ == "__main__":
    main()
'''


# ex-3 simple test
'''
def main():
    test_square()


def test_square():
    assert square(2) == 4
    assert square(3) == 9


if __name__ == "__main__":
    main()
'''

# ex-4 using a dic
'''
def main():
    test_square()


def test_square():
    test_number = {3: 9, 2: 4, -3: 1, 0: 0,}
    for number in test_number:
        try:
            assert square(number) == test_number[number]
        except AssertionError:
            print(f"{number} squared was not {test_number[number]}")
    

if __name__ == "__main__":
    main()
'''

# ex-5 using pytest (no main, try, except, print)

'''
def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
'''


# ex-6 using pytest by creating multiple tests

def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0

# We raise an error
def test_str():
    with pytest.raises(TypeError):
        square("cat")
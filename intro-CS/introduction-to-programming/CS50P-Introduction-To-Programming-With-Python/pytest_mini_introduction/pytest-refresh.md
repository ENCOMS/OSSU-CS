# Pytest mini video

[Edx  - unit test - pytest](https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@b9adc42a712943e798c96981fa2842f5/block-v1:HarvardX+CS50P+Python+type@vertical+block@a6aaece25da443aa96fb346a79b7d98e)

## Pytest

Pytest is a module we can use to test your code more thoroughly.

Code example 1 - convert.py:

```python

def main():
    while True:
        au = input("AU: ")
        try:
            au = float(au)
            break
        except ValueError:
            continue

    print(f"{au} AU is {convert(au)} m")


def convert(au):
    if not isinstance(au, (int, float)):
        raise TypeError("au must be an int or float")
    return au * 149597870700


if __name__ == "__main__":
    main()
    
```

Terminal:

```bash

python convert.py
AU:_

```

At this point is awaiting an input, if we input 1:

 ```bash
 
AU:1
1.0 AU is 149597870700.0 m

```

We could try again, repeating the same steps by hand. That´s why pytest exist.

## Creating a test with pytest and naming conventions 

If we want to write some tests for our code, we have to use some
conventions that per pytest

+ Pytest file should start with either test_filename or filename_test
+ Naming convention for all functions should start with test_
+ The name should have a meaning of what it is testing.

like: test_convert.py

tip:
+ If function convention test_name-of-function is follow pytest would no take it into acount.

## Ways to implement pytest

1. By only unsing keyword assert of pytest, then running the file with pytest.
2. If we need some function from pytest we can import pytest, then use his functions.

## Unit-testing

When we are using pytest we are doing unit testing. It means we are
testing individual units or functions in our program.

## Asserting something

Pytest relies on the idea of asserting something to be true, if not it will let us know.

assert  function(values) == values

Example 2 - test_convert.py

```python
 
import pytest

from convert import convert


def test_conversion():
    assert convert(1) == 149597870700
    assert convert(50) == 7479893535000

```

**Output**

```bash

plugins: typeguard-4.3.0, pylama-8.4.1
collected 1 item                                                                                                     

test_convert.py .                                                                                              [100%]

================================================= 1 passed in 0.02s ==================================================

```

**Note:**
+ pytest will indicate the number of passed or failed tests. In this
case it say it passed 1, since is one function with two assert. If both
assert are true it will be passed.

We can assert many things, in this we can assert if  the function raise an error:

example 3 - raising an error

```python
 
import pytest

from convert import convert


def test_conversion():
    assert convert(1) == 149597870700
    assert convert(50) == 7479893535000

```

**Output**

```bash

plugins: typeguard-4.3.0, pylama-8.4.1
collected 1 item                                                                                                     

test_convert.py .                                                                                              [100%]

================================================= 1 passed in 0.02s ==================================================

```
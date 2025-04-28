# Example 3a - constant variable - variables that can be change.

# ~ def main():

    # ~ MEOWS = 3

    # ~ for _ in range(MEOWS):
        # ~ print("meow")


# Example 3b - constant variable - defining variables constant in classes


# ~ class Cat():
    # ~ MEOWS = 3
    
    # ~ def meows(self):
        # ~ for _ in range(Cat.MEOWS):
            # ~ print("meow")


# ~ def main():
    # ~ cat = Cat()
    # ~ cat.meows()

# Example 4a - type hints - using mypy

# ~ def meow(n: int):
        # ~ for _ in range(n):
            # ~ print("meow")


# ~ def main():
    # ~ number: int = int(input("Number: "))
    # ~ meow(number)


### Example 4b - type hints - return values

# ~ def meow(n: int):
    # ~ for _ in range(n):
        # ~ print("meow")


# ~ def main():
    # ~ number: int = int(input("Number: "))
    # ~ meows: str = meow(number)
    # ~ print(meows)


### Example 4b - type hints - return values

# ~ def meow(n: int) -> None:
    # ~ for _ in range(n):
        # ~ print("meow")


# ~ def main():
    # ~ number: int = int(input("Number: "))
    # ~ meows: str = meow(number)
    # ~ print(meows)


# Example 4d - type hints - return values using hints corrected

# ~ def meow(n: int) -> str:
    # ~ return "meow\n" * n


# ~ def main():
    # ~ number: int = int(input("Number: "))
    # ~ meows: str = meow(number)
    # ~ print(meows, end="")


# Example 5a - docstrings

# ~ def meow(n: int) -> str:
    # ~ '''
    
    # ~ Meow n times
    
    # ~ :param n: Number of times to meow
    # ~ :type n: int
    # ~ :raise TypeError: If n is not an int
    # ~ :return: A string of n meows, one per line
    # ~ :rtype: str
    # ~ '''
    # ~ return "meow\n" * n


# ~ def main():
    # ~ number: int = int(input("Number: "))
    # ~ meows: str = meow(number)
    # ~ print(meows, end="")

# Example 6a - sys argument flags 

# ~ import sys


# ~ def main():
    # ~ if len(sys.argv) == 1:
        # ~ print("meow")
    # ~ elif len(sys.argv) == 3 and sys.argv[1] == "-n":
        # ~ n = int(sys.argv[2])
        # ~ for _ in range(n):
            # ~ print("meow")
    # ~ else:
        # ~ print("usage: meow.py")

# Example 6b - argparse

# ~ import argparse


# ~ def main():
    # ~ parser = argparse.ArgumentParser()
    # ~ parser.add_argument("-n")
    # ~ args = parser.parse_args()

    # ~ for _ in range(int(args.n)):
        # ~ print("meow")


# Example 6c - argparse - adding description and help to arguments

import argparse


def main():
    parser = argparse.ArgumentParser(description="Meow like a cat")
    parser.add_argument("-n", default=1, help="number of times to meow", type=int)
    args = parser.parse_args()

    for _ in range(args.n):
        print("meow")


if __name__ == "__main__":
    main()

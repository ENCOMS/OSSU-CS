"""
In a file called professor.py, implement a program that:

* Prompts the user for a level, 
  - If the user does not input 1, 2, or 3, the program should prompt again.
  - Each level represent a 0-9, 10-99 or 100-999 integers.

* Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 
 digits. No need to support operations other than addition (+).
* Prompts the user to solve each of those problems. 
    - If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem.
    - If the user has still not answered correctly after three tries, the program should output the correct answer.
* The program should ultimately output the user’s score: the number of correct answers out of 10.

Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:



"""

import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):

        x = generate_integer(level)
        y = generate_integer(level)
        result = x + y
        response = 0

        for attempts in range(3):
            try:
                response = int(input(f"{x} + {y} = "))
            except ValueError:
                pass
            if response == result:
                score += 1
                break
            if response != result or attempts == 2:
                print("EEE")
        else:
            print(f"{x} + {y} = {result}")
    print("Score: ", score)


def get_level():
    while True:
        user_input = input("Level: ")
        levels = [1, 2, 3]
        try:
            if int(user_input) in levels:
                return int(user_input)
        except ValueError:
            pass
        else:
            continue


def generate_integer(level):
    match level:
        case 1:
            x = 1
            y = 10
        case 2:
            x = 10
            y = 100
        case 3:
            x = 100
            y = 1000
    return random.randrange(x, y)


if __name__ == "__main__":
    main()

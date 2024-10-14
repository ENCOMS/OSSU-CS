"""
In a file called game.py, implement a program that:

Prompts the user for a level:

- If the user does not input a positive integer, the program should prompt again.
- Randomly generates an integer between 1 and, inclusive, using the random module.

Prompts the user to guess that integer:

- If the guess is not a positive integer, the program should prompt the user again.
- If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
- If the guess is larger than that integer, the program should output Too large! and prompt the user again.
- If the guess is the same as that integer, the program should output Just right! and exit.
"""

import random
import re


def main():
    level_input = user_input("Level: ")

    random_number = random.randint(1, int(level_input))
    print(random_number)

    while True:
        guess = user_input("Guess: ")
        if guess < random_number:
            print("Too small!")
        if guess > random_number:
            print("Too large!")
        if guess == random_number:
            print("Just right!")
            break
        else:
            continue


def user_input(prompt):
    while True:
        answer = input(prompt)
        if input_integer_validator(answer):
            return int(answer)
        else:
            continue


def input_integer_validator(num):
    if num.isalpha() or num == "":
        print("Input need to be a number")
        return False
    elif re.findall("[.]", num):
        print("Input cannot be a float point number")
        return False
    elif re.findall("[-]", num):
        return print("Input cannot be a negative number")
    elif int(num) > 0:
        return True


if __name__ == "__main__":
    main()

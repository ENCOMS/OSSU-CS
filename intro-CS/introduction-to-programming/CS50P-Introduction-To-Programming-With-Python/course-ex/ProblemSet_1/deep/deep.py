"""
# Objective
#   Implement a program that prompts the user for the answer to the Great Question of Life,
# the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively)
# forty-two or forty two. Otherwise output No.

# Note: Be sure to vary the casing of your input and “accidentally” add spaces on either side
# of your input before pressing enter. Your program should behave as expected, case- and
# space-insensitively.
"""

def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ").lower().strip()
    bigQuestion(answer)


def bigQuestion(a):
    match a:
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")


main()
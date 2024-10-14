"""
In a file called figlet.py, implement a program that:

- Expects zero or two command-line arguments:
    - Zero if the user would like to output text in a random font.
    - Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
- Prompts the user for a str of text.
- Outputs that text in the desired font.
- If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.

to install figlet library:
pip install pyfiglet

"""

import random
import sys
from pyfiglet import Figlet


def main():
    figlet = Figlet()  # default font.
    figlet_fonts = figlet.getFonts()  # get list of fonts

    if len(sys.argv) == 1:
        randf = random.choice(figlet_fonts)
        figlet = Figlet(font=randf)
        user_input = input("Input: ")
        print(f"Font: {randf}")
        return print(f"Output: \n {figlet.renderText(user_input)}")

    elif len(sys.argv) > 3:
        sys.exit("Not a valid len")

    elif "-f" != sys.argv[1] != "--font":
        sys.exit(f"Not a valid command: {sys.argv[1]}")

    try:
        if sys.argv[2] not in figlet_fonts:
            sys.exit(f"Not a valid font: {sys.argv[2]}")
    except IndexError:
        sys.exit("Need a valid font")

    user_input = input("Input: ")
    figlet = Figlet(font=sys.argv[2])
    print(f"Font: {sys.argv[2]}")
    print(f"Output: \n {figlet.renderText(user_input)}")


if __name__ == "__main__":
    main()

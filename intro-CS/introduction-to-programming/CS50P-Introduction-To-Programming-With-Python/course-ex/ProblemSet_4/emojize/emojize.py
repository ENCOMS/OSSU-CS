'''
In a file called emojize.py, implement a program that prompts the user for a str in English and then outputs the “emojized” version of that str,
converting any codes (or aliases) therein to their corresponding emoji.
'''

import emoji


def main():
    print(emoji.emojize(input("Input: "), language="alias"))


if __name__ == "__main__":
    main()

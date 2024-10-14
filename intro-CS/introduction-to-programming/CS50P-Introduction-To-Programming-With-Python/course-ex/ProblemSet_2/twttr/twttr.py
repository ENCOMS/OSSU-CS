'''
When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
'''

def main():
    words = input("Input: ").strip()
    shorten_words(words)


def shorten_words(words):
    print("Output: ", end="")
    for char in words:
        match char:
            case "a" | "A" | "e" | "E" | "i" | "I" | "o" | "O" | "u" | "U":
                print("", end="")
            case _:
                print(char, end="")


main()       
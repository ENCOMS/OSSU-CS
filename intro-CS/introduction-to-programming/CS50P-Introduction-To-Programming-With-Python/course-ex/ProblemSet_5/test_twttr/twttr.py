'''
When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr.
In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
whether inputted in uppercase or lowercase.
'''


def main():
    words = input("Input: ").strip()
    print("Output:", shorten(words))


def shorten(words):
    list = []
    for char in words:
        match char:
            case "a" | "A" | "e" | "E" | "i" | "I" | "o" | "O" | "u" | "U":
                pass
            case _:
                list.append(char)
    result = "".join(list)
    return result


if __name__ == "__main__":
    main()
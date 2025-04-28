# Example 9a - using *args for taking any number of arguments

# ~ def main():
    # ~ yell("This", "is", "CS50")


# ~ def yell(*words):
    # ~ uppercased = []
    # ~ for word in words:
        # ~ uppercased.append(word.upper())
    # ~ print(*uppercased)


# Example 9b - using map function and applying str class upper method

# ~ def main():
    # ~ yell("This", "is", "CS50")


# ~ def yell(*words):
    # ~ uppercased = map(str.upper, words)
    # ~ print(*uppercased)

# Example 10a - List comprehension - appling a function

def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)


if __name__ == "__main__":
    main()

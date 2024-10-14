'''
Implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.
'''

def main():
    camel_case_input = input("camelCase: ").strip()
    if len(camel_case_input) == 0:
        return
    else:
        snake_case_converter(camel_case_input)


def snake_case_converter(camel_strings):
    print("snake_case: ", end="")

    for char in range(len(camel_strings)):
        if camel_strings[0].isupper() and char == 0:
            print(camel_strings[0].lower(), end="")

        elif camel_strings[len(camel_strings)-1].isupper() and char == len(camel_strings)-1:
            print(camel_strings[len(camel_strings)-1].lower(), end="")

        elif camel_strings[len(camel_strings)-2].isspace() and char == len(camel_strings)-2:
            print("_", end="")

        elif camel_strings[char].isspace() and camel_strings[char+1].isupper():
            print("", end="")

        elif camel_strings[char].isupper():
            print(f"_{camel_strings[char].lower()}", end="")

        elif camel_strings[char].isspace():
            print("_", end="")

        else:
            print(camel_strings[char], end="")

    print()


main()
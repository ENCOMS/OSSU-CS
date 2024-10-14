'''
In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones.
Among the requirements, though, are:

- “All vanity plates must start with at least two letters.”
- “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
- “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
   The first number used cannot be a ‘0’.”
- “No periods, spaces, or punctuation marks are allowed.”

In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not.
Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not.
Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

Validators:

- First 2 are letters
- Min 2 and Max 6 characters
- Only numbers at the end
- First number cannot be 0
- "." " " "´" are not allowed
- All the six character are letters (This one was is know after a check50)

'''


# Here we are validating the length of the word
def does_min_max_len_is_not_valid(word):
    if len(word) >= 2 and len(word) <= 6:
        return False
    else:
        return True


# Here we are validating punctuation
def does_have_punctuation(word):
    for char in word:
        match char:
            case "." | " " | "´" | "'" | "," | ";":
                return True
            case _:
                continue


# Here we are validating if the first two are letters
def does_first_two_char_are_not_letters(word):
    if word[0].isnumeric() or word[1].isnumeric():
        return True
    else:
        return False


# Here we are validating if the numbers in the second half start with a 0
def does_second_half_start_in_0(word):
    second_half = word[len(word)//2:]
    if second_half[0] == "0":
        return True
    else:
        return False


# Here we are validating if the whole word is a all char, not including numbers
def it_is_a_complete_alpha(word):
    if word.isalpha():
        return True
    else:
        return False


# Here we are validating if the word end with a letter
def does_word_end_with_a_letter(word):
    if word[len(word)-1].isnumeric():
        return False
    else:
        return True


# Here we make the call of all the functions as to give an answer to main
def is_valid(s):
    while True:
        if does_min_max_len_is_not_valid(s):
            return False
        elif does_have_punctuation(s):
            return False
        elif does_first_two_char_are_not_letters(s):
            return False
        elif does_second_half_start_in_0(s):
            return False
        elif it_is_a_complete_alpha(s):
            return True
        elif does_word_end_with_a_letter(s):
            return False
        else:
            return True


def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


main()
from validator_collection import checkers, validators, errors
import sys


def main():
    if len(sys.argv ) == 2:
        print(is_valid(sys.argv[1]))
    else:
        print(is_valid(input("What's your email address? ")))

    
def is_valid(s):
    if not " " in s and checkers.is_email(s):
        if validators.email(s):
            return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()

import re


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    try:
        if len(s) == 2 and s.isnumeric() or s[0].isnumeric() and s[1].isnumeric():
            return False
    except IndexError:
        return False
    try:
        if (
            len(s) == 2
            and s[int(len(s) / 2) :].isnumeric()
            or s[: int(len(s) / 2)].isnumeric()
            and s[int(len(s) / 2) :].isalpha()
        ):
            return False
    except AttributeError:
        return False
    if s[int(len(s) / 2) :].startswith("0"):
        return False
    if len(s) > 4 and s[-1].isalpha():
        return False
    if re.findall("[., ']", s):
        return False
    return True


if __name__ == "__main__":
    main()

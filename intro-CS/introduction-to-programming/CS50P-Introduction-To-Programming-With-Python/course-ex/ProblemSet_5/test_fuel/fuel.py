import re


def main():
    Z = gauge(convert(user_input()))
    print(Z)


def user_input():
    u = input("Fraction: ").strip()
    if len(u) < 0 or re.search("/", u) == None:
        user_input()
    return u


def convert(fraction):
    f1, f2 = fraction.split("/")
    if int(f2) == 0:
        raise ZeroDivisionError("Cannot be divide by 0")
    if not (f1.isnumeric() and f2.isnumeric()) or int(f1) > int(f2):
        raise ValueError("Values must be a number")
    f1 = int(f1)
    f2 = int(f2)
    result = int(round((f1 / f2) * 100))
    return result


def gauge(percentage):
    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"
    return str(percentage) + "%"


if __name__ == "__main__":
    main()

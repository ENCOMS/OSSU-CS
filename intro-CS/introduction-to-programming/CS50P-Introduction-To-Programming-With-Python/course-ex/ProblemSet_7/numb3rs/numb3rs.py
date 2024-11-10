import re
import sys


def main():
    if len(sys.argv) == 1:
        print(validate(input("IPv4 Address: ")))
    else:
        print(f"IPv4 Address: {sys.argv[1]} \n{validate(sys.argv[1])}")


def validate(ip):
    # The pattern was long, so it was separated in multiple lines for clarity.
    pattern = (
        r"^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\."
        r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\."
        r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\."
        r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    )
    if re.search(pattern, ip):
        return True
    return False


if __name__ == "__main__":
    main()

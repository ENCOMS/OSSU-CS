import re
import sys


def main():
    if len(sys.argv) == 2:
        print(count(sys.argv[1]))
    else:
        print(count(input("Text: ")))


def count(s):
    #pattern = r"( um(\.|,|\?)|(?<!\s)(\bum\b)(?<!\s))"
    pattern = r"(\bum\b)"

    if matches := re.findall(pattern, s, flags=re.IGNORECASE):
        return len(matches)
    else:
        return 0
if __name__ == "__main__":
    main()

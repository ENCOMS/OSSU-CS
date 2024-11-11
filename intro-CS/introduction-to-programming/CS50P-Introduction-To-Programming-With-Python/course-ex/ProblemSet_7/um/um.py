import re
import sys


def main():
    if len(sys.argv) == 2:
        print(count(sys.argv[1]))
        # sys.exit(0)
    else:
        print(count(input("Text: ")))
        # sys.exit(0)


def count(s):
    pattern = r"(( +um(\.|,|\?))|((?<!\s)\bum(?<!\s)))"

    if matches := re.findall(pattern, s, flags=re.IGNORECASE):
        return str(len(matches))
    else:
        return "0"


if __name__ == "__main__":
    main()

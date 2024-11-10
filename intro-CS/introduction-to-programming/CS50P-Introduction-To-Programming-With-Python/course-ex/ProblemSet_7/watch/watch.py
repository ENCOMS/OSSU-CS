import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(
        r'\"https?://([a-z]+\.)?[a-z]+\.[a-z]+/[a-z]+/(?P<video_id>[a-zA-Z0-9]+)"', s
    ):
        return f"https://youtu.be/{matches.group('video_id')}"
    else:
        return matches


if __name__ == "__main__":
    main()

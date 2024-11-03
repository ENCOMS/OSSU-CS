# In a file called lines.py,
# 1. implement a program that expects exactly one command-line argument,
# the name (or path) of a Python file, and outputs the number of lines
# of code in that file, excluding comments and blank lines.
# If the user does not specify exactly one command-line argument, or
# if the specified file’s name does not end in .py, or
# if the specified file does not exist, the program should instead exit
# via sys.exit.

# Assume that any line that starts with #, optionally preceded by whitespace,
# is a comment. (A docstring should not be considered a comment.) Assume that
# any line that only contains whitespace is blank.

# Hints

# - Recall that a str comes with quite a few methods, per
# docs.python.org/3/library/stdtypes.html#string-methods, including lstrip
# and startswith.
# - Note that open can raise a FileNotFoundError, per
# docs.python.org/3/library/exceptions.html#FileNotFoundError.
# - You might find it helpful to test your program on, e.g., some of Week 6’s
# source code as well as on programs of your own.

# Outputs sys.exit()
# if sys.argv has no arguments: Too few command-line arguments
# if sys.argv has 1 argument without .py: Not a python file
# if sys.argv has 2 arguments: Too many command-line arguments
# if file is not found: File does not exist
# if sys.argv has 1 argument with .py: number of code lines in the file

import sys


def cmd_arg_validator():
    count = len(sys.argv)

    match count:
        # if sys.argv has no arguments: Too few command-line arguments
        case count if count == 1:
            sys.exit("Too few command-line arguments")
        case count if count == 2:
            # if sys.argv has 1 argument with .py: return the file name
            if ".py" in sys.argv[1]:
                return sys.argv[1]
            # if sys.argv has 1 argument without .py: Not a python file
            else:
                sys.exit("Not a python file")
        # if sys.argv has 2 arguments: Too many command-line arguments
        case _:
            sys.exit("Too many command-line arguments")


def main():
    file_to_read = cmd_arg_validator()
    lines = []
    count = 0

    # try to open file if exist
    try:
        # open and close file
        with open(file_to_read, "r") as file:
            for row in file:
                lines.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")

    # count lines of code then print result
    for line in lines:
        line = line.lstrip()
        if line.startswith("#") or len(line) == 0:
            continue
        else:
            count += 1
    print(count)


if __name__ == "__main__":
    main()

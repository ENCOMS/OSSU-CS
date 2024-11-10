# ~ In a file called scourgify.py, implement a program that:

# ~ Expects the user to provide two command-line arguments:
# ~ the name of an existing CSV file to read as input, whose columns
# are assumed to be, in order, name and house, and
# ~ the name of a new CSV to write as output, whose columns should be,
# in order, first, last, and house.
# ~ Converts that input to that output, splitting each name into
# a first name and last name.
# ~ Assume that each student will have both a first name and last name.

# ~ If the user does not provide exactly two command-line arguments, or
# if the first cannot be read, the program should exit via sys.exit
# with an error message.

# Outputs:
# $ python scourgify.py: Too few command-line arguments
# $ python scourgify.py 1.csv: Too few command-line arguments
# $ python scourgify.py 1.csv 2.csv 3.csv: Too many command-line arguments
# $ python scourgify.py 1.csv 2.csv: Could not read 1.csv


import csv
import sys


def cmd_arg_validator():

    arg = len(sys.argv)

    match arg:
        case arg if arg == 1:
            sys.exit("Too few command-line arguments")
        case arg if arg == 2:
            sys.exit("Too few command-line arguments")
        case arg if arg == 3:
            if ".csv" in sys.argv[1] and ".csv" in sys.argv[2]:
                return sys.argv[1:]
            else:
                sys.exit("One of the files is not a csv file")
        case _:
            sys.exit("Too many command-line arguments")


def main():
    before, after = cmd_arg_validator()
    before_list = []

    try:
        with open(before, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                before_list.append(row)
    except FileNotFoundError:
        sys.exit(f"Could not read {before}")

    with open(after, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])

        writer.writeheader()
        for row in before_list:
            last, first = row["name"].split(",")
            writer.writerow(
                {"first": first.lstrip(), "last": last, "house": row["house"]}
            )


if __name__ == "__main__":
    main()

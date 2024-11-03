# Outputs:
# Too few command-line arguments
# Too many command-line arguments
# File does not exist
# Not a CSV file

import csv
import sys
from tabulate import tabulate


def cmd_arg_validator():
    arg = len(sys.argv)

    match arg:
        case arg if arg == 1:
            sys.exit("Too few command-line arguments")
        case arg if arg == 2:
            if ".csv" in sys.argv[1]:
                return sys.argv[1]
            else:
                sys.exit("Not a CSV file")
        case _:
            sys.exit("Too many command-line arguments")


def main():
    file_to_read = cmd_arg_validator()
    table = []

    try:
        with open(file_to_read, "r") as file:
            information = csv.DictReader(file)
            for row in information:
                table.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(table, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()

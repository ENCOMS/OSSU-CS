## CSV Library - write data to files

# Example 18 - CSV Writer - Assuming order

"""

import csv

def main():
    name = input("What's your name? ")
    home = input("What's your home? ")
    
    with open("students.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow([name, home])

"""



# Example 19 - CSV DictWriter - Not assuming order, only passing a list

import csv

def main():
    name = input("What's your name? ")
    home = input("What's your home? ")
    
    with open("students.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "home"])
        writer.writerow({"name": name, "home": home})

if __name__ == "__main__":
    main()

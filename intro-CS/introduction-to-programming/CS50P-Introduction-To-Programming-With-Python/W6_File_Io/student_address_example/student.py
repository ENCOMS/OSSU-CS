# Example 15 - CSV - too many commas in a row

"""

def main():
    students = []
    
    with open("students.csv") as file:
        for line in file:
            name, home = line.rstrip().split(",")
            student = {"name": name, "home": home}
            students.append(student)

    for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is from {student['home']}")

"""

# Output: ValueError: too many values to unpack (expected 2)


# Example 16 - CSV Library - reader - solving too many commas (corner case)

# Using a single variable in the for loop will store a list of values from the reader
# that needs to be accessed via list index for the appending.



"""

import csv

def main():
    students = []
    
    with open("students.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            students.append({"name": row[0], "home": row[1]})

    for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is from {student['home']}")

"""



# Using two variable in the for loop to store the values from reader and use then
# in the append.


"""

import csv

def main():
    
    students = []
    
    with open("students.csv") as file:
        reader = csv.reader(file)
        for name  , home in reader:
            students.append({"name": name, "home": home})

    for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is from {student['home']}")

"""


# Example 17 - CSV DictReader


import csv

def main():
    
    students = []
    
    with open("students.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"name": row["name"],"home": row["home"]})

    for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is from {student['home']}")

if __name__ == "__main__":
    main()

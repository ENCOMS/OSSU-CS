# Example 10 - Separate Information - CSV - reading two types of value - list


"""

def main():
    with open("students.csv") as file:
        for line in file:
            row = line.rstrip().split(",")
            print(f"{row[0]} is in {row[1]}")

"""


# Example 11 - Separate Information - CSV - reading two types of value - assign then to variables.


"""

def main():
    with open("students.csv") as file:
        for line in file:
            name, house = line.rstrip().split(",")
            print(f"{name} is in {house}")

"""


# Example 12 - Separate Information - CSV - reading two types of value - sorting

"""
def main():
    students = []
    
    with open("students.csv") as file:
        for line in file:
            name, house = line.rstrip().split(",")
            students.append(f"{name} is in {house}")
    
    for student in sorted(students):
        print(student)
"""

# Example 13 - Separate Information - CSV - reading two types of value - sorting (improve version)

"""

def main():
    students = []
    
    with open("students.csv") as file:
        for line in file:
            name, house = line.rstrip().split(",")
            student = {"name": name, "house": house}
            students.append(student)
    
    def get_house(student):
        return student["house"]
    
    for student in sorted(students, key=get_house, reverse=True):
        print(f"{student['name']} is in {student['house']}")


"""

# Example 14 - CSV - sorting with list, dictionary and lambda function

def main():
    students = []
    
    with open("students.csv") as file:
        for line in file:
            name, house = line.rstrip().split(",")
            student = {"name": name, "house": house}
            students.append(student)

    for student in sorted(students, key=lambda student: student["house"]):
        print(f"{student['name']} is in {student['house']}")


if __name__ == "__main__":
    main()

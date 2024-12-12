# Example 11a - list comprehension - sorting


# ~ def main():
    # ~ students = [
        # ~ {"name": "Hermione", "house": "Gryffindor" },
        # ~ {"name": "Harry", "house": "Gryffindor"},
        # ~ {"name": "Ron", "house": "Gryffindor"},
        # ~ {"name": "Draco", "house": "slytherin"},
    # ~ ]

    # ~ gryffindors = [
        # ~ student["name"] for student in students if student["house"] == "Gryffindor"
    # ~ ]
    
    # ~ for gryffindor in sorted(gryffindors):
        # ~ print(gryffindor)

# Example 11b - filter library

# ~ def main():
    # ~ students = [
        # ~ {"name": "Hermione", "house": "Gryffindor" },
        # ~ {"name": "Harry", "house": "Gryffindor"},
        # ~ {"name": "Ron", "house": "Gryffindor"},
        # ~ {"name": "Draco", "house": "slytherin"},
    # ~ ]

    # ~ def is_gryffindor(s):
        # ~ return s["house"] == "Gryffindor"

    # ~ gryffindors = filter(is_gryffindor, students)
    
    # ~ for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
        # ~ print(gryffindor["name"])

# Example 12a - creating dictionary using list comprenhention

# ~ def main():

    # ~ students = ["Hermione", "Harry", "Ron"]

    # ~ gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

    # ~ print(gryffindors)


# Example 12b - creating dictionary using dictionary comprehention

# ~ def main():

    # ~ students = ["Hermione", "Harry", "Ron"]

    # ~ gryffindors = {student: "Gryffindor"} for student in students}

    # ~ print(gryffindors)

# Example 13a enumarate - numeration witout enumarate

# ~ def main():
    # ~ students = ["Hermione", "Harry", "Ron"]
    
    # ~ for i in range(len(students)):
        # ~ print(i + 1, students[i])

# Example 13b enumarate - using enumarate to obtain the two values

def main():
    students = ["Hermione", "Harry", "Ron"]
    
    for i, student in enumerate(students):
        print(i + 1, student)


if __name__ == "__main__":
    main()



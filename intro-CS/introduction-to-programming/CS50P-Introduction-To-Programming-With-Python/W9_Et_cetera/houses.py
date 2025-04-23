# Example 1 - set - filter the duplicates using list and for loops.

# ~ def main():
    # ~ students = [
        # ~ {"name": "Hermione", "house": "Gryffindor"},
        # ~ {"name": "Harry", "house": "Gryffindor"},
        # ~ {"name": "Ron", "house": "Gryffindor"},
        # ~ {"name": "Draco", "house": "Slytherin"},
        # ~ {"name": "Padma", "house": "Ravenclaw"},
    # ~ ]

    # ~ houses = [] # or list() function to create a empty list
    # ~ for student in students:
        # ~ if not student["house"] in houses:
            # ~ houses.append(student["house"])
    
    # ~ for house in sorted(houses):
        # ~ print(house)

# Example 2 - set - filter the duplicates using set function.

def main():
    students = [
        {"name": "Hermione", "house": "Gryffindor"},
        {"name": "Harry", "house": "Gryffindor"},
        {"name": "Ron", "house": "Gryffindor"},
        {"name": "Draco", "house": "Slytherin"},
        {"name": "Padma", "house": "Ravenclaw"},
    ]

    houses = set() # this function will create a set data type
    
    for student in students:
        # Instead of append we use add for set
        houses.add(student["house"])
    
    for house in sorted(houses):
        print(house)
    
    print(houses)
    print(type(houses))

if __name__ == "__main__":
    main()
















































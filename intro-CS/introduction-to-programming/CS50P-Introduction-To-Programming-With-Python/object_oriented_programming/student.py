


# Example 1a - Procedetural programming

# ~ def main():

    # ~ name = input("Name: ")
    # ~ house = input("House: ")
    # ~ print(f"{name} from {house }")
    
    # Example 1b - Functional programming
    # ~ name = get_name()
    # ~ house = get_house()
    # ~ print(f"{name} from {house}")

# ~ def get_name():
    # ~ return input("Name: ")


# ~ def get_house():
    # ~ return input("House: ")


# Example 1c - Functional programming

# ~ def main():
    # ~ student = get_student()
    # ~ print(f"{student[0]} from {student[1]}")


# ~ def get_student():
    # ~ name = input("Name: ")
    # ~ house = input("House: ")
    # ~ return (name, house)


# Example 1d - Functional programming - using dictionarys

    # ~ student = get_student()
    # ~ if student["name"] == "Padma":
        # ~ student["house"] = "Ravenclaw"
    # ~ print(f"{student['name']} from {student['house']}")


# ~ def get_student():
    # ~ name = input("Name: ")
    # ~ house = input("House: ")
    # ~ return {"name": name, "house": house}


# Example 2a - Classes

# ~ class Student():
    # ~ ...

# ~ def main():
    # ~ student = get_student()
    # ~ print(f"{student.name} from {student.house}")


# ~ def get_student():
    # ~ student.name = input("Name: ")
    # ~ student.house = input("House: ")
    # ~ return student

# Example 2a - Classes - Standarized attribute values

# ~ class Student():
    # ~ def __init__(self, name, house):
        # ~ self.name = name
        # ~ self.house = house


# ~ def main():
    # ~ student = get_student()
    # ~ print(f"{student.name} from {student.house}")


# ~ def get_student():
    # ~ name = input("Name: ")
    # ~ house = input("House: ")
    # ~ return Student(name, house)
    
# Example 3a - encapsulate functionalitys - error check

# ~ class Student():
    # ~ def __init__(self, name, house):
        # ~ if not name:
            # ~ raise ValueError("Missing name")
        # ~ if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            # ~ raise ValueError("Invalid house")
        # ~ self.name = name
        # ~ self.house = house


# ~ def main():
    # ~ student = get_student()
    # ~ print(f"{student.name} from {student.house}")


# ~ def get_student():
    # ~ name = input("Name: ")
    # ~ house = input("House: ")
    # ~ return Student(name, house)

# Example 3b - encapsulate functionalitys - printing the student

# ~ class Student():
    # ~ def __init__(self, name, house):
        # ~ if not name:
            # ~ raise ValueError("Missing name")
        # ~ if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            # ~ raise ValueError("Invalid house")
        # ~ self.name = name
        # ~ self.house = house
        
    # ~ def __str__(self):
        # ~ return f"{self.name} from {self.house}"


# ~ def main():
    # ~ student = get_student()
    # ~ print(student)


# ~ def get_student():
    # ~ name = input("Name: ")
    # ~ house = input("House: ")
    # ~ return Student(name, house)


# Example 3c - encapsulate functionalitys - creating our own  custom class methods.

# ~ class Student():
    # ~ def __init__(self, name, house, patronus):
        # ~ if not name:
            # ~ raise ValueError("Missing name")
        # ~ if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            # ~ raise ValueError("Invalid house")
        # ~ self.name = name
        # ~ self.house = house
        # ~ self.patronus = patronus
        
    # ~ def __str__(self):
        # ~ return f"{self.name} from {self.house}"
    
    # ~ def charm(self):
        # ~ match self.patronus:
            # ~ case "Stag":
                # ~ return "🦌"
            # ~ case "Otter":
                # ~ return "🦦"
            # ~ case "Jack Russel terrier":
                # ~ return "🐶"
            # ~ case _:
                # ~ return "🪄"


# ~ def main():
    # ~ student = get_student()
    # ~ print("Expecto Pratonus")
    # ~ print(student.charm())


# ~ def get_student():
    # ~ name = input("Name: ")
    # ~ house = input("House: ")
    # ~ patronus = input("Patronus: ")
    # ~ return Student(name, house, patronus)


# Example 4a - Properties and Decorators - Getter and Setter

# ~ class Student():
    # ~ def __init__(self, name, house):
        # ~ self.name = name
        # ~ self.house = house
        
    # ~ def __str__(self):
        # ~ return f"{self.name} from {self.house}"
    
    # ~ @property
    # ~ def name(self):
        # ~ return self._name
    
    # ~ @name.setter
    # ~ def name(self, name):
        # ~ if not name:
            # ~ raise ValueError("Missing name")
        # ~ self._name = name
    
    # ~ @property
    # ~ def house(self):
        # ~ return self._house
    
    # ~ @house.setter
    # ~ def house(self, house):
        # ~ if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            # ~ raise ValueError("Invalid house")
        # ~ self._house = house


# ~ def main():
    # ~ student = get_student()
    # ~ print(student)
   


# ~ def get_student():
    # ~ name = input("Name: ")
    # ~ house = input("House: ")
    # ~ return Student(name, house)


# Example 6a - clean up student.py with @classmethod 

class Student():
    def __init__(self, name, house):
        self.name = name
        self.house = house
        
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    student = Student.get()
    print(student)
   

if __name__ == "__main__":
    main()



# Example 7a - inheritance
class Wizard():
    def __init__(self, name):
        if not name:
            raise ValueError("Missing Name")
        self.name = name

    def __str__(self):
            return f"{self.name}"

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house
    
    def __str__(self):
        return f"{super().__str__()} from {self.house}"

class Proffesor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def __str__(self):
        return f"{super().__str__()} impart {self.subject}"

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
proffesor = Proffesor("Severus", "Defense Aganist the Dark Arts")

print(wizard)
print(student)
print(proffesor)

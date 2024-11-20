# Example 5a - classmethod - sorting hat - bad design
# ~ import random

# ~ class Hat:
    # ~ def __init__(self):
        # ~ self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    # ~ def sort(self, name):
        # ~ print(name, "is in", random.choice(self.houses))
        

# ~ def main():
    # ~ hat = Hat()
    # ~ hat.sort("Harry")


# Example 5b - classmethod - sorting hat - improve design

import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))
        

def main():
    Hat.sort("Harry")

if __name__ == "__main__":
    main()

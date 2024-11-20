# Example 1a - classes

# ~ class Package():
    # ~ def __init__(self, number, sender, recipient, weight):
        # ~ self.number = number
        # ~ self.sender = sender
        # ~ self.recipient = recipient
        # ~ self.weight = weight

    # ~ def __str__(self):
        # ~ return f"Package number: {self.number}, sender: {self.sender}, recipient: {self.recipient}, weight: {self.weight}"

# ~ def main():
    # ~ packages = [
    # ~ Package(number=1, sender="Alice", recipient="Bob", weight=10),
    # ~ Package(number=2, sender="Bob", recipient="Charlie", weight=5)
          # ~ ]
    # ~ print(packages[0])
    # ~ print(packages[1])

# Example 1b - Instance variables

# ~ class Package():
    # ~ def __init__(self, number, sender, recipient, weight):
        # ~ self.number = number
        # ~ self.sender = sender
        # ~ self.recipient = recipient
        # ~ self.weight = weight

    # ~ def __str__(self):
        # ~ return f"Package {self.number}: {self.sender} to {self.recipient}, {self.weight}kg"


# ~ def main():
    # ~ packages = [
    # ~ Package(number=1, sender="Alice", recipient="Bob", weight=10),
    # ~ Package(number=2, sender="Bob", recipient="Charlie", weight=5)
          # ~ ]
    
    # ~ for package in packages:
        # ~ print(package)


# Example 1c - instance methods

class Package():
    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight

    def __str__(self):
        return f"Package {self.number}: {self.sender} to {self.recipient}, {self.weight}kg"

    def calculate_cost(self, cost_per_kg):
        return self.weight * cost_per_kg


def main():
    packages = [
    Package(number=1, sender="Alice", recipient="Bob", weight=10),
    Package(number=2, sender="Bob", recipient="Charlie", weight=5)
          ]
    
    for package in packages:
        print(f"{package} costs ${package.calculate_cost(cost_per_kg=2)}")


if __name__ == "__main__":
    main()

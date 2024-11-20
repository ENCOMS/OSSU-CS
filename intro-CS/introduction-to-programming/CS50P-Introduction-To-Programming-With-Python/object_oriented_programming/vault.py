# Example 8a - operator overloading

class Vault():
    def __init__(self, galleons, sickles, knuts):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
    
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

def main():
    potter = Vault(100, 50, 25)
    print(potter)

    weasley = Vault(25, 50, 100)
    print(weasley)

# Example 8b - operator overloading - Combining Vaults information simple way

class Vault():
    def __init__(self, galleons, sickles, knuts):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"


def main():
    potter = Vault(100, 50, 25)
    print(potter)

    weasley = Vault(25, 50, 100)
    print(weasley)

    galleons = potter.galleons + weasley.galleons
    sickles = potter.sickles + weasley.sickles
    knuts = potter.knuts + weasley.knuts
    
    total = Vault(galleons, sickles, knuts)
    print(total)

# Example 8c - operator overloading - Combining Vaults information - operator
# overloading way

class Vault():
    def __init__(self, galleons, sickles, knuts):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts  + other.knuts
        return Vault(galleons, sickles, knuts)


def main():
    potter = Vault(100, 50, 25)
    print(potter)

    weasley = Vault(25, 50, 100)
    print(weasley)

    total = potter + weasley
    print(total)


if __name__ == "__main__":
    main()

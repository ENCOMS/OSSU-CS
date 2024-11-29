
def main():
    jar = Jar.get_jar()
    print(f"default capacity: {jar.capacity}, default size: {jar.size}")
    
    while True:
        ask = input("\nPlease select an option: \n" \
                "1. Deposit some cookies. \n" \
                "2. Withdraw some cookies. \n" \
                "3. Exit \n" \
                "Option: "
                )
        if ask == "1":
            jar.deposit(input("How many cookies do you want to put in the jar: "))
            print(f"cookies: {jar}")
        elif ask == "2":
            jar.withdraw(input("How many cookies do you want to take from the jar: "))
            print(f"cookies: {jar}")
        elif ask == "3":
            print("Good Bye")
            break


class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        n = Jar.validate_input(n)
        if n > self.capacity or (n + self.size) > self.capacity:
            raise ValueError("Too many cookies")
        else:
            self.size += n

    def withdraw(self, n):
        n = Jar.validate_input(n)
        if n > self.size:
            raise ValueError("There are not that many cookies")
        else:
            self.size -= n

    @classmethod
    def get_jar(cls):
        try:
            capacity = int(input("Indicate the jar capacity: "))
        except (ValueError, TypeError):
            raise ValueError("Must be integer")
        return cls(capacity)

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        capacity = int(Jar.validate_input(capacity))
        if capacity <= 0:
            raise ValueError("Invalid input: must be greater than 0")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        size = Jar.validate_input(size)
        if size < 0:
            raise ValueError("No cookies")
        self._size = size

    @staticmethod
    def validate_input(value):
        try:
            value = int(value)
        except (ValueError, TypeError):
            raise ValueError("Invalid input: must be a number")
        return value


if __name__ == "__main__":
    main()

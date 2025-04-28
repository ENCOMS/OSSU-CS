
# Example 2a - global variables - UnbounLocalError - balance outside functions

# ~ balance  = 0

# ~ def main():
    # ~ print("Balance:", balance)
    # ~ deposit(100)
    # ~ withdraw(50)
    # ~ print("Balance:", balance)


# ~ def  deposit(n):
    # ~ balance += n


# ~ def withdraw(n):
    # ~ balance -= n


# Example 2b - global variables - UnbounLocalError - balance inside main functions

# ~ def main():
    # ~ balance  = 0
    # ~ print("Balance:", balance)
    # ~ deposit(100)
    # ~ withdraw(50)
    # ~ print("Balance:", balance)


# ~ def  deposit(n):
    # ~ balance += n


# ~ def withdraw(n):
    # ~ balance -= n

# Example 2c - global variables - UnbounLocalError - global keyword

# ~ balance  = 0

# ~ def main():
    # ~ print("Balance:", balance)
    # ~ deposit(100)
    # ~ withdraw(50)
    # ~ print("Balance:", balance)


# ~ def  deposit(n):
    # ~ global balance
    # ~ balance += n


# ~ def withdraw(n):
    # ~ global balance
    # ~ balance -= n

### Example 2d - global variables - UnbounLocalError - oop way

class Account():
    def __init__(self):
        self._balance = 0
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance += n
        
    def withdraw(self, n):
        self._balance -= n


def main():
    account = Account()
    print("Balance: "account.balance)
    account.deposit(100)
    account.withdraw(50)
    print(account.balance)


if __name__ == "__main__":
    main()

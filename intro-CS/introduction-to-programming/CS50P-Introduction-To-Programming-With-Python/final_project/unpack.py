# Example 7a - unpacking - using split

# ~ def main():
    # ~ first, _ = input("What's your name? ").split(" ")
    # ~ print(f"Hello, {first}")


# Example 7b - unpacking - using * on list

# ~ def total(galleons, sickles, knuts):
        # ~ return (galleons * 17 + sickles) * 29 + knuts


# ~ def main():
    # ~ coins = [100, 50, 25]
    # ~ print(total(*coins), "Knuts")


# Example 7c - unpacking - using named parameters

# ~ def total(galleons, sickles, knuts):
        # ~ return (galleons * 17 + sickles) * 29 + knuts


# ~ def main():
    # ~ print(total(galleons=100, sickles=50, knuts=25), "Knuts")


# Example 7d - unpacking - using dictionary

# ~ def total(galleons, sickles, knuts):
        # ~ return (galleons * 17 + sickles) * 29 + knuts

# ~ coins = {"galleons": 100, "sickles": 50, "knuts": 25}

# ~ def main():
    # ~ print(total(**coins), "Knuts")

# Example 8a - unpacking - *args

# ~ def f(*args, **kwargs):
    # ~ print("Positional:", args)

# ~ def main():
    # ~ f(100, 50, 25)

# Example 8b - unpacking - **wkwargs

def f(*args, **kwargs):
    print("Positional:", kwargs)

def main():
    coins = [100, 50, 25]
    print(coins)
    f(galleons=100, sickles=50, knuts=25)


if __name__ == "__main__":
    main()







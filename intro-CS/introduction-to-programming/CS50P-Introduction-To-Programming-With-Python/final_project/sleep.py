
# Example 14a - generators - simple sheep count

# ~ n = int(input("What's n? "))
# ~ for i in range(n):
    # ~ print("🐑" * i)


# ~ def main():
    # ~ n = int(input("What's n? "))
    # ~ for s in sheep(n):
        # ~ print(s)

# ~ def sheep(n):
    # ~ flock = []
    # ~ for i in range(n):
        # ~ flock.append("🐑" * i)
    # ~ return flock

# Example 14c - generator - yield

def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    flock = []
    for i in range(n):
       yield "🐑" * i


if __name__ == "__main__":
    main()

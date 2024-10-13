# Fiftieth example: creating a saying library
'''
def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

main()
'''

# Seventh example: add the 'if __name__ == "__main__"' variable to make sure if not called main, don't execute it.

def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

if __name__ == "__main__":
    main()
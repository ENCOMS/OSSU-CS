
# Names Program that collect names

# 1st interaction, testing input and output

"""
def main():
    name = input("What's your name? ")
    print(f"Hello, {name}")
"""

# 2nd interaction, testing for loops - list append - sort names

"""

def main():
    names = []

    for _ in range(3):
        names.append(input("What's your name? "))

    for name in sorted(names):
        print(f"Hello, {name}")

"""

# 3rd iteraction - Using File I/O - open() function with "w" and write/close methods

"""

def main():
    name = input("What's your name? ")

    file = open("names.txt", "w")
    file.write(name)
    file.close()

"""

# 4rt iteraction - Using File I/O - open() function with "w" and write/close methods

"""

def main():
    name = input("What's your name? ")
    
    file = open("names.txt", "a")
    file.write(f"{name}\n")
    file.close()

"""

# 5st iteraction - Using File I/O - pythonic way to close files, with statement


"""

def main():
    name = input("What's your name? ")

    with open("names.txt", "a") as file:
        file.write(f"{name}\n")

"""


# 6st iteraction - Read back files - .readlines


"""

def main():
    with open("names.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        print("Hello,",  line.rstrip())

"""
        

# 7nd iteraction - Read back files - Python way to combine all for better design


"""

def main():
    with open("names.txt", "r") as file:
        for line in file:
            print("Hello,",  line.rstrip())
            
"""


# 8 iteraction - Read back files - Sorting

"""

def main():
    names = []
    
    with open("names.txt") as file:
        for line in file:
            names.append(line.rstrip())

    for name in sorted(names):
        print("Hello,", name.rstrip())
        
"""
        
# or we can only sort - but we can only do just that and not anything else.

"""

def main():
       
    with open("names.txt") as file:
        for line in sorted(file):
            print("Hello,", line.rstrip())

"""

# 9 iteraction - Read back files - Sorting/Reverse


def main():
    names = []

    with open("names.txt") as file:
        for line in file:
            names.append(line.rstrip())

    for name in sorted(names, reverse=True):
        print("Hello,", name.rstrip())


if __name__ == "__main__":
    main()

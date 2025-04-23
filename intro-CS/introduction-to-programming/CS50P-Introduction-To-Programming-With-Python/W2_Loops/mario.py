### first iteration: simple but functional code:

'''
def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")

main()
'''

### Notes: - We use a for in the function with a _ since we are not gonna use the variable in the iterations. - we use range() as to indicate the times it will iterate.

### second iteration: more simplistic using a pythonic convention.

'''
def main():
    print_column(3)

def print_column(height):
    print("#\n" * height, end="")

main()
'''

### Notes: - we can in python use a multiplier to indicate that the string should be printed X number of times - the end parameter indicates that in the end the space is omitted.


## Horizontal boxes!

### first iteration:

'''
def main():
    print_row(4)


def print_row(width):
    print("?" * width)

main()
'''

#note: - in this we use the same pythonic way of do things in python, but is more elegant and simple since it will print all in the same line.


### first iteration of printing bricks: is ok and works the same in many languages.

'''
def main():
    print_square(3)


def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

main()
'''

### second iteration: we can improve this even further using the pythonic tricks.

'''
def main():
    print_square(3)


def print_square(size):
    for i in range(size):
        print("#" * size)

main()
'''

# in this case it will print 3 times the brinks then the start again in another line and keep printing until the size is reach.


### Third iteration: we can even make abstraction of the problem (making it more smaller)

def main():
    print_square(3)


def print_square(size):
    for i in range(size):
        print_row(size)


def print_row(width):
    print("#" * width)


main()

#the program that calls a functions, don't care how the result is evaluated and return to him, it only wants the results.

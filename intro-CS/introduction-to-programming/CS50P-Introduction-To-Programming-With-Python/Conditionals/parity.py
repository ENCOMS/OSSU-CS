
## First approach:
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True #this is a bool expression
    else:
        return False #this is another bool expression

main()

## Second approach: Pythonic approach, something is pythonic if it's just the way you do things in python.

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return True if n % 2 == 0 else False
    #you can condense in python, and can be read as standard english.


main()

## this is still good, but it can be improve further.

## Third approach: return the same boolean expresion, since it will evaluate and say if true or false in the first place.

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return n % 2 == 0
    # As simple as it seams, the evaluation return a boolean expression if True or False this statement.


main()

# This is one of the more elegant approach we can offer in this case.
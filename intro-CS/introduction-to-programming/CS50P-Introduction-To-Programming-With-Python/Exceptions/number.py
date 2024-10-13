'''
# if we don't finish our declarations:

x = int(input("What's x? ))
print(f"x is {x}")

TERMINAL input/outputs
python number.py

SyntaxError: unterminated string literal (detected at line 4)
'''

'''
#first iteration: not good practice approach
x = int(input("What's x? "))
print(f"x is {x}")


# if we don't enter an int will generate a ValueError

TERMINAL input/outputs
What's x? 50
x is 50

What's x? cat
ValueError: invalid literal for int() with base 10: 'cat'
'''

'''
#second iteration: using try block and exceptions
try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")

# if we enter an string it will output our print on that error.

TERMINAL input/outputs
What's x? 50
x is 50

What's x? cat
ValueError: invalid literal for int() with base 10: 'cat'
'''

'''
#third iteration: we can use better practice and doing the minimum code for do what we need to do.

try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")

# if we enter an string, the try will cath the error, but since it happens before the x equal, x is not define, generating a problem don't the line.


TERMINAL input/outputs
What's x? 50
x is 50

What's x? cat
NameError: name 'x' is not defined
'''

'''
#fourth iteration: we can use else statement as in the if conditionals, this makes handle that defining error work as intended.

try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

# if we enter an string, the try will cath the error if we use something different than a string, in this case we are saying else if not an error print x.


TERMINAL input/outputs
What's x? 50
x is 50

What's x? cat
x is not an integer
'''

'''
#fifth iteration:

while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")
'''

#sixth iteration:

'''
def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x


# A function always should return a value, not a side effect.
'''

'''
# we can even tight this even further

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
            return x
        except ValueError:
            print("x is not an integer")    
'''


'''
# or even further, but it can be arguably complicate the readability of the code, but in short will keep it compact.


def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")    

'''

'''
# we can too pass on the catch of the try as to keep calling until the try is false

def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass
'''

# and lastly we can further improve the function as to not care what is the question, and only to evaluated and return a result. we can achieve this with passing a string as prompt for the function that is being call.

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

main()

# Topic: Exceptions

# Link: https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@bd6e4b312f2b4e8d9e89ec63708a367a/block-v1:HarvardX+CS50P+Python+type@vertical+block@235f477a1c80403e9e6a20e7f29675f6

## What are exceptions
It is when something is exceptional in your program, and actually is not a good thing. It means something has gone wrong, and we should somehow solve.

Things that could go wrong:
SyntaxErrors:
They are problems that are on the programmer to solve from the get-go, as if is not resolve the program will not work.

Some of this are:    
- unfinished literals

number.py
```
x = int(input("What's x? ))
print(f"x is {x}")
```

This will raise an unfinished literal as we din't close our string declaration.

## RuntimeErrors: 
Happens while your code is running, you must write some additional code defensively to detect when those errors happen because you don't necessarily know:
- What input humans are going to type into your program.

ValueError:
- invalid literal for functions

number.py
```
x = int(input("What's x? "))
print(f"x is {x}")
```

What's x? 50
x is 50

What's x? cat
ValueError: invalid literal for int() with base 10: 'cat'

This corner case is that since we declare that the string should be converted to integer base 10 digit, letters cannot be converted to numbers, generating an error.

Solution: program defensively, assume that the users aren't going to be paying attention or, worse, they're malicious, so we want to handle as many errors as we can.

## keyword 'try' and 'except':
With this we can check whether or not something exceptional, something erroneous, has happened.

- try this
- except if this happens do this

number.py
```
try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
```
TERMINAL
What's x? 50
x is 50

What's x? cat
x is not an integer

We as programmers have to anticipated that something exceptional can happen, and actually handle the error for the user, giving them an appropriate error message instead.


except can accept different Value Errors or catch all errors, but is bad practice since it may hide bugs in the code.

the best practice is to figure out what kind of errors may happen and include mention of them explicitly, as if something outside that scope can be deal with too.

Following the best practices, you should only place try in the places that may raise an error.

We need to pay attention on where the error are happening, as if for this example:

number.py
```
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")
```
TERMINAL
What's x? 50
x is 50

What's x? cat
NameError

This indicate that the x is not define, but it really is define, the problem lays in that when the error happens, happens before the = sign, finally no evaluating x, resulting and no x not being define and generating an error of when trying to use it. to resolve this we can use the else statement.

## keyword 'else'
we can use the else keyword as in the if conditionals, as to handle the flow of the code in a more fashioned way.
This makes the code more readable.

number.py
```
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
```
TERMINAL
What's x? 50
x is 50

What's x? cat
x is not an integer

## using loops to keep asking for the correct input:
We use a while loop that will keep asking What is x, until the break statement is reach.
what it means, it keep asking the try/except while true, else if is false in this case no error, pass the keyword break. 

number.py
```
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")
```
TERMINAL
What's x? 50
x is 50

What's x? cat
x is not an integer
What's x?

## using the try/except/else inside a function:

```
def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x
```

A function always should return a value, not a side effect.

we can even tight this even further

```
def get_int():
    while True:
        try:
            x = int(input("What's x? "))
            return x
        except ValueError:
            print("x is not an integer")    
```

or even further, but it can be arguably complicate the readability of the code, but in short will keep it compact.

```
def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")    
```

## keyword 'pass'
it is used to pass or ignoring a catch that was cached. so we dint want to do more than catch.

```
def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass    
```

note: indentation is your best friend on python.

## using promts to the user as to make the functions more readably

the funtions, should not care what we need from the user, as to not hardcode the word to prompt to the user on the function, we can give this same promt to the funcion.


```
def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

main()
```
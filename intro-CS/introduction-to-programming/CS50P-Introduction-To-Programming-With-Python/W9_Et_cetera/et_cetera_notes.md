# Et cetera

What can you do more generally beyond the fundamental concepts.

[Et cetera video](https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@1e2042142d3d4008a6b129c3c3f2a080/block-v1:HarvardX+CS50P+Python+type@vertical+block@9caed2bc85214ec8a099674bdca13d41)

Apart from the fundamental there are other concepts that din't blend
too well with past concepts, as for comprehension they needed more
knowledge.

for example:

## set

In mathematics, a set is a typically a collection of values where in
there are no duplicates. So it's not quite a list.
It's a bit more special that that in that somehow any duplicates are
eliminated for you.

In python is actually a data type, where is useful if you want somehow
automatically filter out duplicates.

Per documentation

docs.python.org/3/library/stdtypes.html#set

Problem: Filtering the duplicates

### Example 1a - set - filter the duplicates using list and for loops

[houses.py#Example1a](houses.py?plain=1#L1)

```python
def main():
    students = [
        {"name": "Hermione", "house": "Gryffindor"},
        {"name": "Harry", "house": "Gryffindor"},
        {"name": "Ron", "house": "Gryffindor"},
        {"name": "Draco", "house": "Slytherin"},
        {"name": "Padma", "house": "Ravenclaw"},
    ]

    houses = [] # or list() function to create a empty list
    for student in students:
        if not student["house"] in houses:
            houses.append(student["house"])
    
    for house in sorted(houses):
        print(house)


if __name__ == "__main__":
    main()
```

Notes:

+ First, we have create a list `students` that have inside a dictionary 
for every student where keys are `name` and `house`.
+ Second, we create a empty list called `houses`, in wich to store the 
house not already inside the list.
+ Third, we create a for loop to iteriate the students list, accesing 
each dictionary with the `house` key, so we can check if the house is 
already on our houses list, if not in, it should be appended.
+ Lastly another for loop for printing, but as we want to sort them too 
we can do this in a pythonic way, using the sorted function in the same 
for loop declaration, then printing each of the houses inside the 
`houses` list.
+ In this case we are reinventing the wheel as python have the means to 
solve this for us.


### Example 1b - set - filter the duplicates using set function.

[houses.py#Example1b](houses.py?plain=1#L20)

```python
def main():
    students = [
        {"name": "Hermione", "house": "Gryffindor"},
        {"name": "Harry", "house": "Gryffindor"},
        {"name": "Ron", "house": "Gryffindor"},
        {"name": "Draco", "house": "Slytherin"},
        {"name": "Padma", "house": "Ravenclaw"},
    ]

    houses = set() # this function will create a set data type
    
    for student in students:
        # Instead of append we use add for set
        houses.add(student["house"])
    
    for house in sorted(houses):
        print(house)
    
    print(houses)
    print(type(houses))

if __name__ == "__main__":
    main()
```

Notes:

+ We change the houses listo to set, in this case using the set funtion
for set creation.

`set()`

+ We can tide the code more, eliminating the if conditional from the for
loop.
+ then we can instead of append to a list, we add to a set:

`houses.add(student["house"])`

+ the rest of the code, in this case the second for loop, and per 
documentation, the set will filter all the duplicates for us.

### Questions - Set
How can you find an item in a set?

Very similar as with a list in the for loop, as `for house in houses`

What happens if you have a similar house name?

If the strings are misspelled or uppercase/lowercase indeed will be a 
different strings, so we to avoid that we could for everyting to 
upppercase, or everyting to lowercase, or capitalize built into str or 
title case that would handle some of the cleanup for us.

## global variables

They are the variables we define outside our functions  that can be
access by all the functions in the file, but down the line, we could
not be able to change those variables as easily as we may think

Problem: bank balance

### Example 2a - global variables - UnbounLocalError - balance outside functions

[bank.py#Example2a](bank.py?plain=1#L1)


```python
balance  = 0

def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)


def  deposit(n):
    balance += n


def withdraw(n):
    balance -= n

if __name__ == "__main__":
    main()
```

Notes:

+ We create a variable outside our functions, so we can access it later
+ We created a main function that call that function outside and print.
+ We later declare 2 more functions that should access that variable
outside, as to update its values.
+ Lastly when we run the program we face a problem, 
`UnboundLocalerror: local variable 'balance' referenced before assignment`
or
`UnboundLocalError: cannot access local variable 'balance' where it is not associated with a value`
+ This indicates that the value is not define inside, since is trying to access a local variables
named balance insted of the global variable.
+ If we try to change a value, it might need to be local to the function.
+ If you try to change a global variable thought in a function it wont work.
+ So, its OK to read a global variable, but apparently, you can't write
to a global variable in the same way.


### Example 2b - global variables - UnbounLocalError - balance inside main functions

[bank.py#Example2b](bank.py?plain=1#L21)

```python

def main():
    balance  = 0
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)


def  deposit(n):
    balance += n


def withdraw(n):
    balance -= n

if __name__ == "__main__":
    main()
```

Notes: 

+ If we define the balance inside main, it will raise too 
UnboundLocalError. Ofcouse in this case is for a different reason, as 
this balance variable is now a local variable of main.

```
def main():
    balance  = 0
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)
```

+ Deposit and withdraw do not have access to that same variable, because
it's local on main.

```
def  deposit(n):
    balance += n


def withdraw(n):
    balance -= n
```

+ So for it to be avalible for every function should be global but, as
before we can't change it.

## global keyword

It's a little different as in other programmed languages, but in python
there is a keyword called global that allows us to tell a function that
this is not a variable that's local to you, we mean it to be a global
variable that we want you to edit.

### Example 2c - global variables - UnbounLocalError - global keyword

[bank.py#Example2c](bank.py?plain=1#L21)

```
balance  = 0

def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)


def  deposit(n):
    global balance
    balance += n


def withdraw(n):
    global balance
    balance -= n


if __name__ == "__main__":
    main()
```

Notes:

+ In this case we take the balance out of main and place it above and 
outside all other functions.
+ Then we declade global keyword + the global variable we want it to
access `global balance`.
+ This indicate to the function that balance is a global function that
is outside the local bounderies and can be accessed and change.
+ We run this version, and indeed is accessing the global variable
correctly.

### Questions - global variable
What happens when you declare a variable globally, and as in the same
variable globally and in a function?

If you declare a variable global, and inside a function you declare a
variable with same name global, the latter will shadow the former.

That, is you'll be able to use the latter, that is the local variable
But it will have no effect on the global variable, because you don't
quite change what you intend to change, creating bugs and reading
problems to other down the line.

What if we decide to add balance as an argument inside the main function?

That is not goin to solve the problem, because if you  pass in a variable
like balance to each of the functions and then change it within that
function, it's only going to be changing in effect a local copy thereof
it's not goin to be changing what's outside of those functions.


### Example 2d - global variables - UnbounLocalError - oop way

[bank.py](bank.py?plain=1#L58)

```python
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
```

Notes:

+ In oop we can model real world entities, for instance a bank, and you 
can model and encapsulate information about that real world entity, for 
instance, like someone's account balance.
+ We start by creating a class named Account. 

`class Acount:`

+ We then define the class init dunder, in this case only with self, 
since we are not taking any values, and self indicate the class 
instance.

`def __init__(self):`

+ we create an instance variable calle balance and declare that would 
start with 0.

`self.balance = 0`

+ Since we are not taking values and we want this value to be private 
we need to change the name to include a visual clue to ourself that 
this variable is private and I, or other code should not touch.

`self._balance = 0`

+ We define a function called `def balance(self)` that really is goint to be a 
property whose purpose in life is just to `return self._balance`
+ To make balance function to work as a property, we need to use the
decorator `@property` above the function. 
```python
@property
def balance(self)
    return self._balance
```
+ We define a function `deposit(self, n)` that will take a number, where 
it will we call the instance variable and add n `self._balance += n.`
+ We define a function `withdraw(self, n)` that will take a number, where 
it will we call the instance variable and minus n `self._balance -= n.`
+ We define main, where we declare a instance of Account class called 
account. `account = Account()`
+ then we print the balance, accesing the property of the instance class
account with a dot balance. `print("Balance:", account.balance)`
+ we use the deposit method inside our instance function to add 100.
`account.deposit(100)`
+ then we withdraw using the withdraw method.
`account.withdraw(50)`
+ then we print the balance property.
`print(account.balance)`
+ lastly we include the if init dunder equal to main to run main.
```
if __init__ == "__main__":
    main()
```
+ The previus example worked fine using global keyword, but that's not 
the best form of encapsulation we have at our disposal.
+ By declaring a self variable, this can be accessed by the functions
inside the class.
+ The rule of the thump is to use global variables sparengly as to
reduce bugs, logic, or reading errors, since problems escalate quicktly.

### Questions - Global variables:
What does property does?
is an instance variable that is somehow protected, it allows to us to
control what it can read and write.
In this case @property functions as a getter, that means to retrive
a value not change.

## Constants variable:
+ Are  variables that once set, cannot be change later
+ It allows to program defensively, preventing errors or malicius change.
+ In python since it work on the honor system there are ways to change it.

### Example 3a - constant variable - variables that can be change.

```python

def main():

    MEOWS = 3

    for _ in range(MEOWS):
        print("meow")

if __name__ == "__main__":
    main()

```


Notes:
+ in the for loop since we dont need an iterator variable (i) we can use
underscore _ , indicating in a python way that we are not gonna use the
iterator variable.
+ using range(3) will indicate that will run as far as three times, but
since the number 3 is hardcode there could be problems of interpretation
as for why 3 down the line.
+ by using a variable we can assign a name and value to the 3
and keep it at the top of the code, that way we only change the value
in one place.
+ The variable names should be all capitalize as to indicate that is
indeed a variable that should not be change.
+ There is a problem, where we can change this value later on and still
allows us to do that, there is a keyword in other languages to prevent
that from happening but in python there is only the honor system.


### Example 3b - constant variable - defining variables constant in classes

```python

class Cat():
    MEOWS = 3
    
    def meows(self):
        for _ in range(Cat.MEOWS):
            print("meows")


def main():
    cat = Cat()
    cat.meows()


if __name__ == "__main__":
    main()

```

Notes:
+ we define a class Cat
+ We create a class variable not an instance variable.
+ The class variable with have the name all capitalize to indicate that 
the class variable is a constant variable.
+ We create a instance method that will only take self as argument, 
inside we create the for loop but in this case the range would be
`range(Cat.MEOWS)` where Cat indicate the class, MEOWS, that we want to
access the contents of the class variable MEOWS.
+ we instanciate the class creating a cat of class Cat `cat = Cat()`
+ where we use the instance method that will print the quantity inside
class variable MEOWS `cat.meows()`
+ But this still dont protect the variable to be change. since python
is not actually enforcing that it should not be change.


## type hints

Since python is a dynamically typed language, not strongly typed, where
python dynamically figure out what type of variable it is, without use
telling what it should expect to store in a variable.

For c++ or java a programmer need to specify what types of variables you
want sometgthing to be.

Upside of that it can create problems if you want to store some diffent
type of value in the same variable, where the language helps in figure
out the mistakes for you.

Python does not enforce this, but you as a programmer can use a tool
that will tell you or not you're using a variable correctly or not
before realise the code to the world.

A very popular program that helps detect that is `mypy` that check whether or not
your code is adhering to your own type hints.

to install:
pip install mypy

poetry add mypy

documentation:
mypy.readthedocs.io

### Example 4a - type hints - using mypy

```python

def meow(n: int):
        for _ in range(n):
            print("meow")


def main():
    number: int = int(input("Number: "))
    meow(number)


if __name__ == "__main__":
    main()

```

Notes:

+ we create a simple function that take n as argument and a loop that use
that value to print meows.
+ we ask the user for an input of a number, but if not converted to an int
it will raise TypeError, str cannot be interpreted as integer, this means
that the str that input passed to the variable is not an int.
+ We can place a hint in the function like this:
`def meow(n: int)` where `: int` indicate to python that it should expect
an int, but python dont care since it wont enforce that for us.
+ if we use a program like mypy that can undertands hints, we can obtain
a more complete information of what go wrong in our code.
+ This program is intended for the programmer, not the user.
+ if take the habit to anotate the variables we are using, mypy will
do a better job in finding the particular problem is affecting our code.
like when we are asking the user for a number but we are taking is a str
`number: int = input("Number: ")`
+ Now as the problem has been found, we can convert the input to int
so we can safely pass the value as an argument for the funtion meow.
`number: int = int(input("Number: "))`
+ With this the code can run as intended.

### Questions - type hints

It is common to use type hints, or is used only in more complex code?
+ python as it was intended, it was intended for easy write and code,
but wont enforce too many rules.
+ strong type checks are good thing for the correctness of the code, 
because programms like mypy can help detect problems before even the
code is even run.
+ It tends to be a good for defensive programming.
+ So for python is essentially that we annotate the types this way,
so we can use programs like mypy to check those hints.
+ depending of code manager or team, they may very well try to use
type hints to decrease the probability of bugs.


### Example 4b - type hints - return values

```python
def meow(n: int):
    for _ in range(n):
        print("meow")


def main():
    number: int = int(input("Number: "))
    meows: str = meow(number)
    print(meows)


if __name__ == "__main__":
    main()
```


Notes:
+ In the case we wanted to use unit test, we should instead of getting a 
side effect, we should expect a return value that we could test.
+ for example that we create a variable str meows that take the return
value of the funtion meow that can be print later, this could be tested
correctly with unit test.
+ By default when a function in python does not explecitly return a value,
its implicit return value is in effect none.
+ so running the code will indeed print 3 meows and none as we are
mistakely printing the defaut return of the function meow that is none.


### Example 4c - type hints - return values using hints

```python

def meow(n: int) -> None:
    for _ in range(n):
        print("meow")


def main():
    number: int = int(input("Number: "))
    meows: str = meow(number)
    print(meows)

```

Notes:
+ We can annotate the return value of a function using "->" then the
expected return value. `def meow(n: int) -> None`
+ Like this we can use now mypy to check for errors, indeed catching the
problem of the return value of none of meow.


### Example 4d - type hints - return values using hints corrected

```python

def meow(n: int) -> str:
    return "meow\n" * n


def main():
    number: int = int(input("Number: "))
    meows: str = meow(number)
    print(meows, end="")


if __name__ == "__main__":
    main()
```

Notes:
+ We change the hint of return value of the funtion to str
`def meow(n: int) -> str:`
+ then we change the insides of the function to use a pythonic way of
using strings, using \n for new line and * n as to multiply the str,
then returning this to the print function.
+ since we are adding a newline, we need to fix added new line of the
function print, changing the named argument end to empty, `end=""`

### Questions - type hints

How does the multiply works on strings?

Is a multiply overload of the string type, where a string to the left
is multiply be the number of the right, concatenating them.

Can we not typeast this data type of this variable number?

No, where the correct terminology, it wouldn't be called typecasting in
this context because is not C or C++ where there's an equivalence
between these types.

Here we use int() function to convert the number str to integer, and the
: int as a hint not the function. so we have to do the convertion 
ourself.


## docstrings

document strings, where in python per pep-0257 python enhancement proposal,
that essentially standardizes how you should document your functions
among other aspects of your code.

link of the reference:
peps.python.org/pep-0257

### Example 5a - docstrings

```python

```

Notes:
+ We go back to the meow function and start documenting the code.
+ the standard way of doing this is using doc string notation.
+ This comments are created not above, instead inside of it.
+ We dont use simple onliner comments, we use thriple quotes or double
quotes, (""") or ('''), at the start and end.
+ by doing this and adhere to this type of documenting your code, we can
use tools that can extract this comments and even generate wed pages,
reducing this way having to this all manually.
+ For docstrings, we use more than one line, so for all that to work,
we start the first line with thriple quotes, then in the next lines we
write what we need than close in a another line with another thriple
quotes.
```
    """
    text
    """
```
+ we use in docstrings a type of convention know as restructured text, 
which is a form of markdown-like language that's used for documentation,
for websites, for blogs, and even more.
```
:param m:
:type n:
.
.
.
```
+ this dont have anything to do with type hints, since type hints is a
feature of python, and docstrings is adhering to a third party convention
of putting in between a python doc string from the start to the end
a certain standard format so that these third party tools can analyze my
code for me top to bottom, left to right, and ideally generate
documentation for me.
+ It can generate pdf, a webpage, or something else, so that my colleagues
don't need to not just only write code but also manually create documentation
for our code.
+ We can keep everyting together and use tools to generate the same for us.

### Questions - docstrings

So when you say you would document it and put it in a PDF, is the 
purpose of doing this to publish it and share your function so other 
users can use it?

+ Absolutely, searching for internet we can find many examples of pdf or
webpages created with this tools as to share with other what the program
do, so we dont waste time trying to infer what a function do exist for.

+ So it just tends to be much more developer-friendly to have a proper
documentation for our own code or libraries as well.

Does the docstring includes any of the code?

Yes it can be done, not with the convention used before, but we can
indeed include sample of the code, like samples with input and samples
of output.

This other convention and tools will run the code, check your sample 
inputs run aganist the sample outputs and check that everyting is valid 
to document, if not it will warning you that there is a bug in the 
code.


## sys arguments flags

What if we want to enter the number via command line?
+ Where if the program have not arguments print 1 meows and if sys 
arguments take the number of times, print number of times meow.
+ It's very common to provide what are often called switches or flags, 
whereby you pass in something like -n, which semantically means this 
number of times, then often a space, and then something like the number 
3.
+ This allows to do other things at the command line if we want. But 
the fact that we have standardized on how we are providingcommand line 
arguments to the program make it more reliable, knowing what does the 
three mean, where it is more meaningful that the name of the file then 
3.

### Example 6a - sys argument flags 

```python

import sys


def main():
    if len(sys.argv) == 1:
        print("meow")
    elif len(sys.argv) == 3 and sys.argv[1] == "-n":
        n = int(sys.argv[2])
        for _ in range(n):
            print("meow")
    else:
        print("usage: meow.py")


if __name__ == "__main__":
    main()

```

Notes:
+ We import sys, so we can have access to `sys.argv`
+ we then use len() to know the quantity of values are in `sys.argv`
+ we access them like a list with [] from 0 to the number of arg take 
in.
+ We use if ... elif ... else to determinate the len and values we need 
for every option, no arg, 3 arguments representing the flag and number 
of times will be repeated the meow, and the default if none of the 
options are present.
+ -n or other letter can be a valid flag, where --number is more common
for whole words.
+ but in a bigger program, that is more complicated, many flags can get 
messy pretty fast, as what option go first, with or witout name, etc.
+ to help with this cases, there is a library called argparse.

## argparse library

This library is of very common use when the code gets more complicated, 
or when we want to allow the user to pass in configuration options at 
the commnad line.

argparse comes from argument parse, to parse something means to read 
it, kind of pick it apart to analyze it.

### Example 6b - argparse

```python
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n")
    args = parser.parse_args()

    for _ in range(int(args.n)):
        print("meow")


if __name__ == "__main__":
    main()

```

Notes:
+ we import the library argparse
+ we create an object argparse using the constructor of the class.
`parser = argparse.ArgumentParser()`
+ We then indicate to the argparser the specific command line arguments
that we want to support in our program.
`parser.add_argument("-n")`
+ Now we can parse the command line arguments with method `.parse_arg` 
in `parser.parse_arg` where argparse is going to do the import of sys, 
check the list of arguments and valided that indeed there is a valid 
argument inside then assign to another variable object called args.
`args = parser.parse_args()`
+ argparser will figure out, anyway the user introduce any flags or 
argument in any order for us.
+ we can then create a for loop that have in range the transformation
to integer of the n property in args object.
```python

for _ in range(int(args.n)):
    print("meow")

```
+ it all work if we use `python meows.py -n 3`, argparser is doing its
work correctly, but if the user wont cooperate, in this case dont
introduce a valid argument, it will generate an error like TypeError.
+ To solve problems of not valid arguments or none at all, argparser
provide some documentation of how to solve the problem. In this case it
provides access to a help flags that will inform of what the program
can accept as valid arguments, could be short `-h` or named `--help`.
+ If not show much information until is configure correctly but it is a
start to make the program more useful.
+ `[-h]` square bracket as almost always in documentation means it's
optional.


### Example 6c - argparse - adding description and help to arguments

```python

import argparse


def main():
    parser = argparse.ArgumentParser(description="Meow like a cat")
    parser.add_argument("-n", default=1, help="number of times to meow", type=int)
    args = parser.parse_args()

    for _ in range(args.n):
        print("meow")


if __name__ == "__main__":
    main()

```

Notes:
+ we can add a description to the program, changing the named parameter 
`description`, adding information of the program.
`description="Meow like a cat"`
+ we can add more information to the help on the argument we are adding
changing the help parameter  in the add_argument.
`parser.add_argument("-n", help="number of times to meow")`
+ This much wont do as much if no valid argument is not found, so in 
the documentation of argparse we can add a default value in this case 
would be 1.
```
default=1

parser.add_argument("-n", default=1, help="number of times to meow")
```
+ we can even specify that the argument should be and int. By specifing 
that the argument should be int, will do the work for us to take input 
and pass it back already transformed to us as the type we wanted, so we 
wont need to that manually.

```python
type=int

parser.add_argument("-n", default=1, help="number of times to meow", 
type=int)

```

### Questions - argparse

What does args.n contain?
It contains the integer that the human typed after a space dash n.

What happends if the type for the argument is not an int?

argparse will generate an automatic error menssage that will help find
the problems.

## unpacking

Is a feature of python that unpack a list or some other data structure
and putting it immediately into two or more variables.

### Example 7a - unpacking - using split

```python

def main():
    first, _ = input("What's your name? ").split(" ")
    print(f"Hello, {first}")


if __name__ == "__main__":
    main()

```

Notes:
+ by using split, after the input, we can obtain two values that were
join by an space.
+ first, _ = indicate that the values generated by the split function, 
will be store in the variables first and _ , where first would be name 
and underscore _ will store the rest where in this case would be 
discarded.
+ them using print to print the first value that was unpacked by split.
+ This aproach is very simple and wont support edge cases so is very
fragil.

### Example 7b - unpacking - using * on list

```python

def total(galleons, sickles, knuts):
        return (galleons * 17 + sickles) * 29 + knuts


def main():
    coins = [100, 50, 25]
    print(total(*coins), "Knuts")


if __name__ == "__main__":
    main()

```

Notes:
+ we create a function that takes three arguments, galleons, sickles, knuts.
+ we use * with the list to tell python to unpack the contents of the 
list in the function total(). `*coins`
+ lastly it print the return value of the function total.

### Questions - unpacking .split and * star unpack for list:

Does that work for tuples, sets, dicts?

for list, tuples, enumerations
not for set as it dont preserve the order.
dictionary use other conventions.

Can you unpack to get values and make mathematics?

No, you should unpack them individualy values, of each specific location
and operate on them.

What if we declare some default values, and the list is bigger than what
the functions expect?

It will generate a TypeError since function total takes 3 positional 
arguments but 4 are given.


### Example 7c - unpacking - using named parameters

```python

def total(galleons, sickles, knuts):
        return (galleons * 17 + sickles) * 29 + knuts


def main():
    print(total(galleons=100, sickles=50, knuts=25), "Knuts")


if __name__ == "__main__":
    main()

```

Notes:
+ By especifing the names of the parameters, we now are in the presence
of named parameter, since we are using the names that in the function.
`print(total(galleons=100, sickles=50, knuts=25), "Knuts")`


### Example 7d - unpacking - using dictionary with two star **

where we use pair key and values

```python

def total(galleons, sickles, knuts):
        return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50, "knuts": 25}

def main():
    print(total(**coins), "Knuts")


if __name__ == "__main__":
    main()

```

Notes:
+ in this case, we unpack dictionarys using not one, two star ** with
the name of the dictionary. this will unpack in a way that resemble
the way we define named parameter, where galleons=100, sickles=50, knuts=25
`print(total(**coins), "Knuts")`


### Questions - unpaking using star * for list and ** for dictionary

Can we have more pair key values inside of the dictionary?

Yes, but in this case the unpack will return 4 key=value, generating
a TypeError since the function only expected 3.

If we declared a default value in the function, if we use asterick, will
it overwrite the value or will skip that default value?

It will indeed overwrite the values as we are passing values to those 
parameters, in that case if we give fewer arguments, like 2, it will 
work since we have a default value, but in this case it will generete 
an TypeError.

## Asterisk in python *args, **wkwargs

They are not only use to unpack list or dictionary, we can encounter them
in python own documentation as parameter like `*args`, `**wkwargs`

using *args and **kwargs in functions allows us to take any amount of
positional arguments or keyword arguments, so we can with it bypass
limitations of hardcode variables that could potentialy create problems
if the quantity min or max is pass.

### Example 8a - unpacking - *args

```python

def f(*args, **kwargs):
    print("Positional:", args)

def main():
    f(100, 50, 25)


if __name__ == "__main__":
    main()

```

Notes:
+ We create a function that will take any amount of positional arguments
and keyword arguments, that will print the input arguments.

```python

def f(*args, **kwargs):
    print("Positional:", args)
    
```
+ Then we use this function on main, inputting 3 positional arguments,
where the functions print those values.

```python

def main():
    f(100, 50, 25)

```

+ running the program, will return then a tuple of the arguments we
pass on to the function.
`Positional: (100, 50, 25)`

### Example 8b - unpacking - **wkwargs

```python

def f(*args, **kwargs):
    print("Positional:", kwargs)

def main():
    f(galleons=100, sickles=50, knuts=25)


if __name__ == "__main__":
    main()

```

Notes:
+ we change to kwagrs in the printing
+ we then create name arguments and assign values on the function will
with the use of **kwargs in fact create a dictionary for us when we print.

`f(galleons=100, sickles=50, knuts=25)`

result

`Positional: {'galleons': 100, 'sickles': 50, 'knuts': 25}`

### Questions - *args, **wkwargs

What will happen if you print kwargs and the argument is like a list?

it should give an error since **kwargs would try to intepret a key and value
pair, where in the list there is only values.

If we store the values in a variable coins and print we can see the
list of valus inside the variable coins.

Can you pass the kwargs from one function to another function?

Yes, you can pass either of those to another function, which you might 
want to do if you want to wrap another function, provide some 
additional functionality but still pass in all the supported arguments 
to the underlying function as well.

## Types of programming

We started on procedural programming, then functional programming then
object oriented programming.

## functional programming - map

### Example 9a - using *args for taking any number of arguments

Yell program, that allow the user an input and yell the response.

```

def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


if __name__ == "__main__":
    main()

```

Notes:
+ we create main and inside we call a function yell where we pass to it 
three arguments, three strings.
`yell("This", "is", "CS50")`
+ bellow we define the yell function, in this case we want to accept
any amount of arguments so we use 1 asterisk argument.
`def yell(*words):`
+ then we create a list where we gonna store all the string properly
uppercased, so we can print them at the end.
`uppercased = []`
+ as for uppercasing every str argument, we use a for loop, where we 
append to the new list, the corresponding str, uppercased with upper 
function.
```python
for word in words:
        uppercased.append(word.upper())
```
+ at the end we print the list, but we use 1 asterisk, in this case to
unpack the list so it can be print by print the print function.
`print(*uppercased)`

## map

It allow us to map, that is, apply some function to every element of 
some sequence like a list.

Link of the documentation:

docs.python.org/3/library/functions.html#map

Per documentation:

map(function, iterable, ...)

### Example 9b - using map function and applying str class upper method

```python

def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)


if __name__ == "__main__":
    main()

```

Notes:
+ we eliminated the list and the loop, so we can create a new variable.
+ In the new variable, we will assign the map to it, where map takes two
arguments, 1 function, and the iterable object.
+ since we need to upper case, and we know str is a class that contains
the upper method that we need, we call the class str, and access the upper
method. `map(str.upper)`
+ the next argument, will be the words, in this case the any number of 
arguments that are passed to the function yell, will be passed to map 
function. `map(str.upper, words)`
+ this is what powerfull of map, and functional programming, where map
function takes str.upper function and apply it to the arguments passed,
where we can ommit having to do this manually.

## List comprehension

Refer to the ability in python for us to very easily construct a list on
the fly witout using a loop, without calling append, and append but to
do everyting in one liner.

Is the oportunity to create a list, using square brackets, but inside 
of those square brackets to write a python expression, that in effect 
is going to dynamically generate a brand new list for you using some 
logic you've written.

Many programmers love this python capability to define on the fly a list
inside of which is any number of values that you would ordinarily, at least
in the start construct with a loop and again calling append, and append, etc.
but that usually takes two, three, four or more lines.

The list comprehension reduce all that to fewer lines.

### Example 10a - List comprehension - appling a function

```python

def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)


if __name__ == "__main__":
    main()

```

Notes:
+ like before we have the same example of yell, but in this case we change
only the part with map, to include now the list comprehension syntax.
+ we create a simple list first, where inside we include the expression
of what we want to do and ultimately store in the list.

`uppercased = []`

then

`uppercased = [word.upper() for word in words]`

+ reading from left to right, for each word in words, upper case word
and store in the list.

### Questions - list comprehension - appling a function

Can you do conditionals, like if else or combinations?

Yes, you can.

Is this functional programming, in this particular thing?

Not necessarilly, is more of feature of python.
 
### Example 11a - list comprehension - sorting

```python

def main():
    students = [
        {"name": "Hermione", "house": "Gryffindor" },
        {"name": "Harry", "house": "Gryffindor"},
        {"name": "Ron", "house": "Gryffindor"},
        {"name": "Draco", "house": "slytherin"},
    ]

    gryffindors = [
        student["name"] for student in students if student["house"] == "Gryffindor"
    ]
    
    for gryffindor in sorted(gryffindors):
        print(gryffindor)

if __name__ == "__main__":
    main()

```

Notes:
+ Where we have a list of dictionarys, where we want to find each 
gryffindor student and save the names in a another list.
+ we create the new list, but inside we use the list comprehension 
using what we know on loops in combination of what we know of 
conditionals to create an expression that will retrive the names of 
each student in gryffindor.
+ where if read left to rigth, for student in students, if student house
is gryffindor, do save student name in the list.
```

gryffindors = [
        student["name"] for student in students if student["house"] == "Gryffindor"
    ]

```

+ lastly a for loop to iterate with the list and print the names in sorted
order
```

for gryffindor in sorted(gryffindors):
        print(gryffindor)

```

## filter library

it will generate a the same effect but with a more functional approach.

Documentation:

docs.python.org/3/library/functions.html#filter

Per documentation

filter(function, iterable)

### Example 11b - filter library

```python


```

Notes:
+ we create a function that only purpose is to return a true or false.
```

def is_gryffindor(s):
        return s["house"] == "Gryffindor"

```
+ tip if the result of comparation is true of false, the function 
should return the comparation result, not necessarilly have to give 
back a true or false statement.
+ filter takes at least two arguments, one which is the name of the 
function to call is gryffindor and we are going to apply that function 
to each of the elements of the sequence.

`gryffindors = filter(is_gryffindor, students)`

+ Its similar in spirit to map, where we are passing a function that's 
going to be applied to each of the elements in the sequence, but map 
returns one values for each element in the sequence, thats how we 
forced all of the words uppercase in past example.
+ Filter expects its first function to be not something like str.upper,
but a function that returns true or false.
`gryffindors = filter(is_gryffindor, students)`
+ then we use a for loop to print each of gryffindor name. where we sort
using sorted but in this case we use the key named parameter to 
indicate we want to sort by name since this is not a simple list, is a 
list of dict.

`for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):`

+ lastly we print the the name of each student from the list of dict
that was sorted.

`print(gryffindor["name"])`

### Questions - on list comprehension vs filter

+ If we write a code with list comprehension, where the expression was in
one line, would style checkers have a problem with it because it's is less
readable?

It will reformat to  a style code, but if we proactive try to write code
as black will format, it will change little of what we writed.

+ When using filter, instead of callind is_gryffindor name, can we call
the function right in there inside filter?

No, if we type is_gryffindor() we are indeed ourself calling, but we want
filter to call it for us, so we only use the name is_gryffindor

+ Can you write the return as house == Gryffindor inside the filter?

Yes, with lambda functions, since when we want to pass in a quick and
dirty function anonymously like in the sorted to filter by a dictionary
key of a dictionary.

We can do that in the filter too like

`gryffindor = filter(lambda s: s["house"] == "Gryffindor", students)`

Like this we don't bother to define a function only to then use it in one
and only one place.

## dictionary comprehention

With dictionary comprehension we can create dictionarys on the fly, a 
dictionary with keys and some values without having to do it old-school 
by creating an empty dictionary, and creating a for loop, and iterating 
over that loop and inserting more and more keys and values into the 
dictionary, where we can rather doit all at once.

### Example 12a - creating dictionary using list comprenhention

```python

def main():

    students = ["Hermione", "Harry", "Ron"]

    gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

    print(gryffindors)

```

Notes:
+ We eliminate previous code and instead we are going to create the list of dictionary
of the students.
+ first we create a list of names.
`students = ["Hermione", "Harry", "Ron"]`
+ second we create a new list variable where we use list comprenhention.
`gryffindors = []`
+ the list comprenhention takes first the final result i want then the
syntax of how to obtain each individual value, in this case a for loop.
`gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]`

If we want one bigger dictionary that have each name as key and gryffindor
as value.

### Example 12b - creating dictionary using dictionary comprehention

```python

def main():

    students = ["Hermione", "Harry", "Ron"]

    gryffindors = {student: "Gryffindor"} for student in students}

    print(gryffindors)


if __name__ == "__main__":
    main()

```

Notes:
+ for dictionary comprehention, one indicator is that instead of having
square brackets outside we have curly braces.
+ What we want inside the curly braces?, to be key every student name, 
and value Gryffindor and we want to do this for every student in 
students.
`gryffindors = {student: "Gryffindor"} for student in students}`
+ This is another manifestation of how readable python is from left to right.


## enumarate

Enumerate allows you to solve numeration problems much more simply by
iterating over a sequence, but findind out not each value one at the a time,
but both the value one at a time and the index thereof.

It gives back two answers at once.

Documentation:
docs.python.org/3/library/functions.html#enumerate

Per documentation:
enumerate(iterable, start=0)

### Example 13a enumarate - numeration witout enumarate

```python

def main():
    students = ["Hermione", "Harry", "Ron"]
    
    for i in range(len(students)):
        print(i + 1, students[i])


if __name__ == "__main__":
    main()

```

Notes:
+ in this case we can number each student using a for loop, but
in this case we use  i for store the number of times in range.
that way we can access each student name from the list using the
number of index, plus we can use that same i + 1 to give them a rank.
```

for i in range(len(students)):
        print(i + 1, students[i])

```

### Example 13b enumarate - using enumarate to obtain the two values

```python

def main():
    students = ["Hermione", "Harry", "Ron"]
    
    for i, student in enumerate(students):
        print(i + 1, student)


if __name__ == "__main__":
    main()

```

Notes:
+ for this we create a for loop that generate 2 variables , i, for index
and student for the student name that are inside students.
`for i, student in enumerate(students):`
+ with enumarate as per documentation will read the list and return not
only the current index but the current value.
+ lastly we print the index + 1 so to resemble ranks, and the name.

## generators

give us the ability to generate values in python.
It can create massive amount of data for the users, but we can have it
return just a little bit of that data at a time.

Documentation:
docs.python.org/3/howto/functional.html#generators

Per documentation:
def generate_ints(N):
   for i in range(N):
       yield i
       
Where `yield` keyword is the generator function that is detected by 
python.

We can create a program to count sheeps as example.

### Example 14a - generators - simple sheep count

```python

n = int(input("What's n? "))
for i in range(n):
    print("🐑" * i)

```

Notes:
+ we create a simple program that counts and print sheeps in range of 
what the user input.

### Example 14b - generators - improving with current knowledge

```python

def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock

if __name__ == "__main__":
    main()

```

Notes:
+ define a main function with the if to call main
+ we need helper funtions to factoring our code as to abstrac away 
functionality
+ we should keep logic away from main, as to give us change to use
unit testing later on.
+ And since the functions should do the logic and work, and main only
should print the results, we should do the work of creating the sheeps
and handend then back to main to print.
+ for this we create a list inside sheep function and we create a for
loop as to append the many times the user passed on to sheep, the sheeps
to store in flock, lastly returning the list flock at the end.

```
def sheep(n):
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock
```
+ since we took out the sheep logic, now in main we can print the retults
of sheep using another for loop.

```
for s in sheep(n):
        print(s)
```

### Questions - generators - simple sheeps

what is happending when the input is too big like 1000000?

We are passing the limit of cpu and memory our computer or pc to handle
the problem at hand.

So to solve that issue, it should print one at the time, but that will 
take us a step back of what we know, for this we have generators. Like 
say before it can create massive amount of data for the users, but we 
can have it return just a little bit of that data at a time.

### Example 14c - generator - yield

```python

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

```

Notes:
+ changing the logic in the sheep function, we eliminate create a list
then return that value, instead we use a simple for loop and use yield.
+ Yield will work as return, but return one value at a time, return one
value at a time, this way the for loop will continue to work, handing
back only a little piece of data at a time.
```
for i in range(n):
    yield "🐑" * i

```
+ with this the program wont hand, waiting to process all the sheeps
at once, but work with one row of sheeps at the time.

## yield - iterator

+ Yield is returning an iterator that allows your code, your own for loop
in main to iterate over these generated values one at a time.

### Questions - generators - yield

+ How does this yield actually works under the hood?

Under the hood, the generator is just retaining state for you. it does 
not going to run the entire loop from top to bottom and then return a 
value. Its going to do one iteration and y yield a result.

For python, is going to suspend the function, but remenber on what 
iteration it was. so the next time you iterate over it, as it is going 
to happend in the for loop, you get back another value again and again.

So yield returns, indeed, this thing called an iterator and that 
iterator can be stepped over in a loop one element at a time, where 
python handle all this for us.

+ So if every iteration, the program will return the memory to the system
so the program will not crash?

Correct, is only trying to return the current value of i, not trying to return
all millions rows of the same, so it use fewer memory to work.



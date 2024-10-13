# Course: CS50's Introduction to Programming with Python

## Topic: Functions, Variables

[Link to course in edX CS50P](https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@744dad66fcce478a92fb1073b3d373fa/block-v1:HarvardX+CS50P+Python+type@vertical+block@50897469e09545f29c4535c6ffb2c704)

### What is a text editor?

A text editor is a program for writing text and save it in the right format. They are simple without enhanced capability.

### What is a code editor?

Newer, modern text editor like Sublime text, notepad++, visual code have 2 major advantages, syntax highlighting for most popular programming languages. And the second, their immense extensibility. Meaning that while they can look simple at first, installing the right extension can make them super powerful and useful.

[Link for reference on code editors 1](https://medium.com/@sgarcia.dev/learn-webdev-series-coding-tools-part-1-introduction-ides-vs-text-editors-and-the-rise-of-the-75c74bf26988)
[Link for reference on code editors 2](https://blog.jetbrains.com/webstorm/2024/03/ides-vs-code-editors/#:~:text=Simply%20put%2C%20a%20code%20editor%20is%20a%20more,your%20workflow%20with%20the%20help%20of%20AI%20features.)

In the course cs50p we use vscode since is an text editor with IDE capability.

### What is an IDE?

An IDE (Integrated Development Environment) is software that combines commonly used developer tools into a compact GUI (graphical user interface) application. It is a combination of tools like a code editor, code compiler, and code debugger with an integrated terminal.

[Link for reference on IDE on gfg](https://www.geeksforgeeks.org/what-is-ide/)

### Why we cannot use rich or enhanced word processing software for coding?

We need to be weary of rich format text editors like google docs and Microsoft Word since they add a lot more functions like, bold, italic, bullet points, that are of no use for writing code.
tf 0:50

### How to create a python file in vscode?

In vscode terminal we type the command "code" name and format:

```shell
code hello.py
```

+ "This will create a temporally file name hello with an extension .py, this file wont be store until we saved it on the ssd"

We then write a line of code on the file:

```python
print("hello, world")
```

+ "Especial text editors, like vscode have features that allow to autocomplete sentences, and can be extended more with many extensions they have to offer"
tf 2:15

+ "When programming we mostly use text editor and CLI (command line interface)"
tf 2:57

### How to run a python file in vscode?

If we are not there yet, we need to navigate to the folder on where the file reside. Can be done doing right click in the file explorer and click on Open in integrated terminal.

Now we can execute the file with the command python:

```shell
python hello.py
```

tf 3:53

### What is python interpreter?

To run the command python, we must have installed something that is called an interpreter that is free to download, in this case a python interpreter that can handle the process of reading top to bottom, left to right, translating the code to zero and ones that the computer can understand.
tf 5:00

**Output:**

```shell
hello, world
```

### What are functions?

Is like an action or a verb that lets us do something in the program. Any language comes with some predetermined set of functions, some very basic actions or verbs that the computer will already know how to do for us, and the programmer can use those functions at will to get the computer to do those things.
tf 5:51

In this case we are using the function print to show something on the terminal.

A function is a reusable block of code that performs a specific action. It can accept input values, known as parameters, and can also return a value as a result.

```python
print("hello, world")
```

```terminal
$> hello, world
```

### How helpful is a function?

Functions help to break down complex problems into simpler, manageable tasks, making the code more readable and maintainable.

### What is an argument?

Is an input to a function that somehow influences its behavior.
tf 6:30

Is any input that a function can take and do something with it.

### What is a side-effect?

It can be visual, audio or something that can appears on the screen like the output of the print function or saving on disk.
tf 7:06

A side effect occurs when a function or expression modifies something outside its local scope. These modifications can include:

+ Changing the value of a non-local variable.
+ Modifying a static local variable.
+ Altering a mutable argument passed by reference.
+ Raising errors or exceptions.
+ Performing I/O operations (like reading/writing files or interacting with databases).
+ Invoking other functions that have side effects.

### What is a bug?

Is a mistake in a program and that can take so many forms, but ultimately are problems for you to solve.
tf 7:50

If we don't finish the way the language expects, it may not run at all.
tf 8:50

### What is the print function?

Is a function that is use to print an argument on the screen.

### What it is input function?

It prompt the user for an input with blinking cursor waiting for them to type something.
tf 12:45

Is a function that allow to take inputs from the user using the keyboard.

By documentation the input function can take an argument itself.
tf 13:16

Example of input taking an argument:

```python
input("What's your name")
```

+ "By itself it is correctly, but since we are not storing nor return the value for printing, it won't do anything".

### What is a return value?

Is a feature some functions have, it gets the input, process it and then hand it back to the programer so it can do something with it.

But to be useful it may need to be store in a variable for later use.
tf 15:38

### What is a variable?

A variable is a container for some value inside the computer. The value can be a number, text an image or video or more.
tf 15:57

Since is programming and not mathematics, we can name the variable with a more descriptive term to describe what it is.
tf 16:28

Is a container that holds a value, as simple as text or numbers or more complex like list or objects that can change.

### What is the assignment operator?

A single equal (=) in programming is the assignment operator, it is use to assignment some value to a variable.
tf 17:04

We can store a value or an input, so as to reuse it later.
tf 17:37

```python
name = input("What's your name?")
print("Hello, David")
```

Variable: name  
Assignment operator: =
Function: input(Argument)

### What is a comment?

Comments are notes to yourself in your code. The computer ignores the comment so it won't break the code. This way we can explain the code to a teacher, a colleague, or yourself.
tf 20:45

+ "To represent a single line that will be commented we use the "#", for multiple lines use """, only for multiline we have a start and finish of the comment."

```python
# Ask user for their name
name = input("What's your name?")

# Say hello to the user
print("Hello,")
print(name)
```

+ "We can use comments too to create pseudocode to express the idea or thoughts succinctly, methodically, algorithmically".
tf 22:58

```python
# Ask user for their name

# Say hello to the user
```

+ "Pseudocode is a nice way of structuring your to-do list, especially if you have no idea how to write the code you want, because it breaks a bigger program down into small bite-sized tasks".
tf 23:46

### What is string?

"A string is a list of characters in order.

A character is anything you can type on the keyboard in one keystroke, like a letter, a number, or a backslash.

Strings can have spaces like in “hello world”.

An empty string is a string that has 0 characters.

Python strings are immutable

Python recognize as strings everything that is delimited by quotation marks (” ” or ‘ ‘)".

[Link to reference on PFB](https://www.pythonforbeginners.com/basics/strings)

### What does the input function expect?

Input function per documentation it only expects a string (text), later we can change the data types as needed.
tf 24:16

By using + operator and , to call the separator on the print() function plus the input from the user, we can create more dynamic strings.

### How + operator work in Print function?

+ When using + operator with a string, we are concatenating (joining strings together) tf 27:50

```python
# Ask user for their name
name = input("What's your name? ")

# Say hello to user
print("hello, " + name)
```

### How , separator work in the Print Function?

+ When using , separator we are invoking the default separator of the print function, this way we can show, many items and display them on the same line. tf 28:25

```python
# Ask user for their name
name = input("What's your name? ")

# Say hello to user
print("hello,", name)
```

It invoke the print function default separator, this join strings with an space between, allowing to display them on the same line, however we can customize this too.

+ In case of + operator it will not add an space since is doing a concatenation, instead the , separator will add one space since this is his default behavior defined in the function Print.

### What is the Technical Term for Strings?

"the technical term for strings in python and many other languages is STR" tf 31:37

### How can we change a function parameters?

We can change a function behavior by checking the documentation. tf 32:53

In python case it can be found in docs.python.org.

### How can we change Print function parameters?

checking the print function documentation:
docs.python.org/3/library/functions.html#print
tf 33:24

print() function as show in the documentation:

```python
print(*objects, sep=' ', end='\n', file=sys.stdout flush=false)
```

tf 33:37

Where we can identify the parameters:

+ ```print``` Name of the function

+ ```()``` Parentheses, everything inside the parentheses is a potential argument in this case parameters.

+ ```*objects``` it means it accept any type of objects. tf 35:00

+ ```sep=' '``` Separator with empty space ' ' or anything we want if modified tf 35:35

+ ```end='\n'``` end of the function, in this case \n indicates new line, this means that at the end it will create a new line or anything we want if modified. tf 36:05

Example of changing the named parameter END:

```python
# Ask user for their name
name = input("What's your name? ")

# Say hello to user
print("hello,", end="")
print(name)
```

```shell
$ python hello.py
What's your name?
hello, David
```

So we can say that changing the end from new line to empty space will place the next print in the same line, then at the end of that print use his default new line to place the cursor in the next line. tf 39:00

We can use ' ' or " " indifferently but we should be consistent with your uses. tf 40:00

### What is difference between argument and parameter?

+ When we are checking a documentation, the arguments in this case are called parameters to the function.

+ When we are talking to What we can Pass to a function, those inputs are called Parameters.

+ When we actually use the function and pass in values inside of those parentheses those inputs, those values are arguments.

+ So to speak we are talking the same thing, but the terms we use change depending of the different direction you look at the problem. tf 35:04

a. What the function can take can be called parameter
b. What you pass to the function can be called arguments

"When defining a function, the variables listed inside the parentheses in the function definition are known as parameters. These act as placeholders for the values that will be passed to the function. When the function is actually called, the values supplied to it are known as arguments."

[link of reference](https://www.bing.com/search?q=what+is+a+parameter+in+python&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=what+is+a+parameter+in+python&sc=10-29&sk=&cvid=2D3F0722A0354B58BC0EC6FED7302B9E&ghsh=0&ghacc=0&ghpl=)

### Types of parameters a function can have?

+ **Positional parameter:** In a sense that since the first thing you pass to print gets printed first. The second thing we pass to print after a comma gets printed second and so forth. tf 40:25

+ **Named parameters or keyword parameters:** Like SEP, END in print function, they are optional and can be passed at the end of the print statement or also use them by name. tf 40:48

+ **Default Arguments:** Python allows functions to have default argument values. If the function is called without the argument, the default value is used.

```python
# Function with default arguments
def add_numbers(a=7, b=8):
    sum = a + b
    print('Sum:', sum)

# Function calls with varying number of arguments
add_numbers(2, 3) # Both arguments provided
add_numbers(a=2) # Only 'a' provided, 'b' uses default value
add_numbers() # No arguments provided, both defaults are used
```

**Output:**

```console
Sum: 5
Sum: 10
Sum: 15
```

+ **Arbitrary Arguments:** Sometimes, you may not know beforehand how many arguments will be passed to your function. Python allows you to handle this by defining functions with arbitrary numbers of arguments using the *args (position arguments) and **kwargs (keyword arguments) syntax.

```python
# Function with arbitrary number of arguments
def find_sum(*numbers):
    result = 0
    for num in numbers:
        result += num
    print("Sum =", result)

# Function calls with different numbers of arguments
find_sum(1, 2, 3)
find_sum(4, 9)
```

**Output:**

```console
Sum: 6
Sum: 13
```

In the ```find_sum``` function, ```*numbers``` allows the function to accept any number of arguments, which are accessible as a tuple within the function.

[link for reference on argument and parameters](https://www.bing.com/search?q=what+is+a+parameter+in+python&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=what+is+a+parameter+in+python&sc=10-29&sk=&cvid=2D3F0722A0354B58BC0EC6FED7302B9E&ghsh=0&ghacc=0&ghpl=)

### How can we use quotes inside quotes?

This is a corner case with quotes, we can use quotes inside quotes if we use a different one outside and inside
```print("hello 'david'")``` tf 42:13

or we can use the escape character \

```print("hello \"david\"")``` tf 42:37

### How to format a string in python?

There is a feature in python that format a string in a special way. tf 44:25

Python provides several methods to format strings, allowing for dynamic string creation by inserting variables and expressions into a string template. Among the most commonly used methods are f-strings, the format() method, and the modulo operator (%).

[link for reference](https://www.bing.com/search?pglt=169&q=How+to+format+a+string+in+python%3F&cvid=d69f22d3832649878bf86f8e052cbfac&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7MgYIARBFGDkyBggCEEUYOzIGCAMQRRg7MgYIBBBFGDsyBggFEEUYQTIGCAYQRRg9MgYIBxBFGD0yBggIEEUYPdIBCDEyNDlqMGoxqAIIsAIB&FORM=ANNTA1&PC=U531)

### f-strings

When we can add an "f" before the string, and inside the string we use curly braces {} to envelop a variable, this way we can can replace later. tf 44:31

"..is a concise and readable way to embed expressions inside string literals"

"f-strings are great for readability and performance but do not support lazy evaluation."

```python
# Ask user for their name
name = input("What's your name? ")

# Say hello to user
print(f"hello, {name}")
```

```python
name = "Alice"
formatted_string = f"Hello, {name}!"
print(formatted_string) # Output: Hello, Alice!
```

### format() method

"The format() method is versatile and supports lazy interpolation, making it suitable for creating templates that can be filled later."

by documentation:
format(format_string, /, *args, **kwargs)

It takes a format string and an arbitrary set of positional and keyword arguments.

```python
greeting = "Hello"
name = "Bob"
formatted_string = "{}, {}!".format(greeting, name)
print(formatted_string) # Output: Hello, Bob!
```

### % module operator

The modulo operator is an older method that is less commonly used in modern Python but is still useful to know for maintaining legacy code. The modulo operator is simpler but offers fewer formatting options

```python
name = "Charlie"
formatted_string = "Hello, %s!" % name
print(formatted_string) # Output: Hello, Charlie!
```

Instead of of the f and curly braces from f-strings we have the module % and value to denote where and what to replace with.

+ %d replace numbers.
+ %s replace strings.
+ %.2f replace float with a two digit precision.

### Eager interpolation

In eager interpolation, Python inserts the values into the string at execution time in the same place where you define the string.

### Lazy interpolation

In lazy interpolation, Python delays the insertion until the string is actually needed. In this latter case, you create string templates at one point in your code and fill the template with values at another point.

[link for reference en eager and lazy inter.](https://realpython.com/python-string-interpolation/#:~:text=In%20eager%20interpolation%2C%20Python%20inserts%20the%20values%20into,fill%20the%20template%20with%20values%20at%20another%20point.)

### Difference between format methods

Each method has its own set of features and use cases.

+ f-strings are great for readability and performance but do not support lazy evaluation.
+ The format() method is more flexible and allows for both eager and lazy interpolation.
+ The modulo operator is simpler but offers fewer formatting options.

When choosing a string formatting method, consider the specific needs of your code and the version of Python you are using. For most modern Python applications, f-strings or the format() method will be the preferred choice.

### What are methods in python?

"In Python, a Function is a block of code that accomplishes a certain task. A function inside a class and associated with an object or class is called a Method.

Similar to functions, methods also have a name, parameters, and a return statement. Classes can bundle data and functionality together. We use methods to provide the functionality to a class."

We can access a method just like an attribute by using the dot operator and either the object name or the class name depending on the type of the method.

[link for reference on methods on python geeks](https://pythongeeks.org/methods-in-python/)

### What methods can we use with strings?

In the documentation we can find many methods to use on a string.

docs.python.org/3/library/sdtypes.html#string-methods

We can manipulate the strings to concatenate, clean, reformating and more. tf 46:25

### .strip() method

```python
# Ask user for their name
name = input("What's your name? ")

# Remove whitespace from str, it will eliminate spaces at the start and end of the string
name = name.strip()

# Say hello to user
print(f"hello, {name}")
```

tf 47:50

the strip() in str will eliminate white spaces at the start and end of the string. In str there are lot of functions that can be accessed with a dot, and this functions are called methods.
tf 48:05

### .capitalize() method

To further refine the output, so as to capitalize the name, we can use another method called capitalize(). tf 50:00

```python
# Ask user for their name
name = input("What's your name? ")

# Remove whitespace from str, it will eliminate spaces at the start and end of the string
name = name.strip()

# this will take the string and Capitalize the first character
name = name.capitalize()

# Say hello to user
print(f"hello,", {name})
```

In the case it will capitalize the first letter of the string but not the first letter of the second word, for this we can use another method called title(), that in fact do this for us. tf 51:47

### .title() method

This method capitalize each first character of a word in a string.

```python
# Ask user for their name
name = input("What's your name? ")

# Remove whitespace from str, it will eliminate spaces at the start and end of the string
name = name.strip()

# this will take the string and Capitalize the first character
name = name.title()

# Say hello to user
print(f"hello, {name}")
```

### .split() method

It split a string into multiple smaller substrings.
tf 57:43

```python
# Ask user for their name, remove whitespace, capitalizing
name = input("What's your name? ").strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")

# Say hello to user
print(f"Hello, {first}")
```

Now we are indicating to use the split method on the string inside the variable name, indicating that it will do it when it finds an empty space " ", in this case the result should be the name and last name and we can actually, in python, assign both of those values from that sequence at once to some variables. tf 58:43

### What is method chaining?

We can optimize the code, so it can be easy to read, typing in one line both methods chaining them together. tf 53:05

Method chaining refers to calling multiple methods sequentially on the same object in a single expression. Each method call returns an object, often the same object (modified or not), allowing the subsequent method to operate on that object.

In method chaining, the result of one method call becomes the context for the next method. This allows for concise and readable code, especially when working with objects that require several transformations or operations.

[link for reference on method chaining in gfg](https://www.geeksforgeeks.org/method-chaining-in-python/)

```python
# Ask user for their name
name = input("What's your name? ")

# Remove whitespace from str and capitalize user's name
name = name.strip().title()

# Say hello to user
print(f"hello, {name}")
```

We can even optimize more using the methods in the input before storing in the variable in first place tf 53:15

```python
# Ask user for their name, remove whitespace, capitalizing
name = input("What's your name? ").strip().title()

# Say hello to user
print(f"hello, {name}")
```

We can strive to have code to be a lot tighter, neater, and easy to read. tf 53:28

So to reiterate, a method is a function that's built in to a type of value tf 54:00

We can combine many methods, but at some point it can get unreadable. tf 54:31

Ultimately is subjective, depending on our own preferences or your company or group guidelines, at the end of the day it depends on your opinion to choose one style or the other. tf 57:45

### What is the int data type?

Is short for integer. It is all numbers toward negative or positive infinity, but there is no decimal point. tf 59:58

### What types of operators python support?

Operators are used to perform operations on variables and values.

Python divides the operators in the following groups:

+ Arithmetic operators
+ Assignment operators
+ Comparison operators
+ Logical operators
+ Identity operators
+ Membership operators
+ Bitwise operators

### Arithmetic operators

Arithmetic operators are used with numeric values to perform common mathematical operations

```console
Operator    Example          Same As
+           Addition         x + y
-           Subtraction      x - y
*           Multiplication   x * y
/           Division         x / y
%           Modulus          x % y
**          Exponentiation   x ** y
//          Floor division   x // y
```

+ % modulo allows you to take the remainder after dividing one number by another.
+ ** power raises the thing on the left to the power of the right.
tf 1:44:55
+ // Floor division, also known as integer division or whole number division, is a mathematical operation that divides two numbers and returns the largest possible integer

### Assignment operators

Assignment operators are used to assign values to variables

```console
Operator    Example        Same As
=           x = 5          x = 5
+=          x += 3         x = x + 3
-=          x -= 3         x = x - 3
*=          x *= 3         x = x * 3
/=          x /= 3         x = x / 3
%=          x %= 3         x = x % 3
//=         x //= 3        x = x // 3
**=         x **= 3        x = x ** 3
&=          x &= 3         x = x & 3
|=          x |= 3         x = x | 3
^=          x ^= 3         x = x ^ 3
>>=         x >>= 3        x = x >> 3
<<=         x <<= 3        x = x << 3
:=          print(x := 3)  x = 3
                           print(x)   Walrus operator
```

### Comparison operators

Comparison operators are used to compare two values:

```console
Operator    Name                       Example
==          Equal                      x == y
!=          Not equal                  x != y
>           Greater than               x > y
<           Less than                  x < y
>=          Greater than or equal to   x >= y
<=          Less than or equal to      x <= y
```

### Logical operators

Logical operators are used to combine conditional statements

```console
Operator   Description                Example
and        Returns True if both
           statements are true        x < 5 and  x < 10
or         Returns True if one of 
           the statements is true     x < 5 or x < 4
not        Reverse the result, 
           returns False if the 
           result is true             not(x < 5 and x < 10)
```

### Identity operators

Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

```console
Operator   Description                      Example
is         Returns True if both 
           variables are the same object    x is y
is not     Returns True if both variables
           are not the same object          x is not y
```

### Membership operators

Membership operators are used to test if a sequence is presented in an object

```console
Operator    Description                    Example
in          Returns True if a sequence
            with the specified value is
            present in the object          x in y
not in      Returns True if a sequence
            with the specified value is
            not present in the object      x not in y
```

### Bitwise operators

Bitwise operators are used to compare (binary) numbers:

```console
Operator   Name    Description                  Example
&          AND     Sets each bit to 1 if 
                   both bits are 1              x & y
|          OR      Sets each bit to 1 if 
                   one of two bits is 1         x | y
^          XOR     Sets each bit to 1 if 
                   only one of two bits is 1    x ^ y
~          NOT     Inverts all the bits         ~x
<<         Zero    Shift left by pushing
           fill    zeros in from the right
           left    and let the leftmost 
           shift   bits fall off                x << 2
>>         Signed  Shift right by pushing
           right   copies of the leftmost
           shift   bit in from the left, 
                   and let the rightmost
                   bits fall off                x >> 2
```

[link for reference on operators](https://www.w3schools.com/python/python_operators.asp)

### What is interactive mode?

Python allows to run the interpreter directly from the terminal, allowing a sort of conversation back and forth with the computer, translating immediately. tf 1:02:09

### How int works?

first we create a new file:

```shell
code calculator.py
```

```python
x = 1
y = 2

z = x + y

print(z)
```

tf 1:04:05

This a representation of what some basic math can be done, but if we want it to make more interactive we could use part of what we know from previous examples.
tf 1:04:43

```python
x = input("What's x? ")
y = input("What's y? ")

z = x + y

print(z)
```

In this case we are in presence of a bug, since the input() only accept strings, the + add operator is concatenating the two strings, since they are strings not integers at the moment.
tf 1:05:30

To resolve this we can use the int() function, since in python _is not only a type of data, is a function_. This way we can transform an string to the integer version of the input.
tf 1:07:01

```python
x = input("What's x? ")
y = input("What's y? ")

z = int(x) + int(y)

print(z)
```

If we create a variable to only use it once, it is not that compelling, instead we could try to include the operation inside the print function.
tf 1:08:25

```python
x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)
```

### How can we nest functions?

In this case we are nesting functions, we can put a function call that is the use of a function inside of the use of another function so that the return value of the inner function becomes the argument to or the input to the outer function.

Same as in math, first it get results from the inner parenthesis, then the result gets evaluated be the outermost function.
tf 1:09:35

Like in math, first we resolve the most inner to the outer parentheses

### What we need to prioritize writing code?

+ We need to prioritize readability
+ Making the code readable for someone else is very good thing. This help the future you, not waste time trying to remember what you did.
+ Simplicity, keep the code simple.
tf 1:13:15

+ If the code gets too complicated, making you think too much any time you read it, you are wasting time.
+ A complicate code, increase the probability of mistakes and tactical mistakes or logical errors in your code.
tf 1:14:04

+ Make comments useful.

### What is the float data type?

Is a number with a decimal point value. In Math is a real number that has a decimal point in it. tf 1:15:05

```python
x = float(input("What's x? "))
y = float(input("What's y? "))

print(x + y)
```

It represent all real numbers with a decimal point, with a limited precision by computer resources. It's too a conversion function.

### What is the round function?

It takes an input a number and then rounds it for us, for instance, to the nearest integer, but per documentation we can change this behavior. tf 1:16:05

[Link for round function documentation](docs.python.org/3/library/functions.html#round) tf 1:16:30

```console
round(number[, ndigits]) 
```

tf 1:16:44

This show us the name function but its available parameters as well, and the inputs that we can provide when using this function.
tf 1:16:57

We can identify the following:

+ round is the name of the function
+ number is the first argument, and is a number, and only that. In this case we are talking of a positional parameter.
+ In documentation, when we find [] the contents inside are optional.
+ [, ndigits] specify the number of decimals tf 1:17:58

```python
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

print(z)
```

+ This time, it would be valid to separate in another line the code, so we can have a more cleaner thought process. tf 1:20:10

### How to change a number to use thousand separator with f-strings?

We can give a format to the number, using the f-strings, since this allows dynamic string generation based on variable values or the results of expressions.

```python
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

print(f"{z:,}")
```

tf 1:21:55

```console
What's x? 10
What's y? 100
1,000
```

+ In this case we are using : to left of the variable to indicate that the number gonna be format with a , each thousand.

#### What is float limitations?

+ Float cannot represent numbers infinitely, because computers only have so much memory, they only have finite amount, so at some point, they're going to have to round the number. tf 1:22:34

```python
x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

print(z)
```

output:
0.6666666666666

+ Unlike other languages in python there is not upper bound on how big an INT can be, but float is bound by how precise a floating point value can be. tf 1:23:42

### Rounding using round function with ndigits optional parameter

```python
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x / y, 2)

print(z)
```

In this example we are rounding per documentation of the function round() to 2 digits precision.

### Rounding using f-strings

```python
x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

print(f"{z:.2f}")
```

Doing the same with the string format, we can have the same results as the rounding format with the 2 digits point. In this case we are formatting the values on the variable z to have 2 float point value. tf 1:25:43

### How to define functions?

In python an any other languages we can create our own functions, especially design to solve the same kind of problem we have solve before that maybe is not define by default or especially tailored to our needs.
tf 1:26:49

First step is to assume the function already exist and build the code around it. tf 1:27:38

```python
name = input("What's your name? ")

hello()

print(name)
```

At this point it will raise an NameError if we execute since hello() is not define yet. tf 1:28:30

For creating a function we need to use a keyword DEF

### def keyword

DEF is short for define, is use to create our own functions.
tf 1:28:45

We define this new functions atop everything else, so it can be accessed later on. tf 1:29:04

```python
def hello():
....code

name = input("What's your name? ")

hello()

print(name)
```

We can identify the following:

+ def is the keyword for creating functions

+ hello name of the function at our own discretion

+ () parentheses is where we place the arguments or no arguments at all

+ : identify that from this point the function body start.

+ .... Indentation, everything is define after the function in an indentation.

tf 1:29:13

```python
def hello():
    print("hello")


name = input("What's your name? ")

hello()

print(name)
```

output:
hello
David

It looks odd, so at this point we may try to parameterize the function, so it say hello and the name in the same line.
tf 1:30:55

```python
def hello(to):
    print("hello,", to)

name = input("What's your name? ")
hello(name)
```

We add to the function a parameter with the name "to" only because we can and it sound right for the circumstance, since in english can be read as "hello to". tf 1:31:30

So in this case when we use the function hello(name), we are passing an argument, in this case the variable called name, so that the variable gets passed into the hello function. tf 1:32:49

When the function itself is called the computer assumes that same value is now called To. So name is essentially copied to another variable called To, so in that context Hello, we can say Hello to that variable instead. tf 1:33:13

### How to define the default parameters of a function?

We can give to the functions we created, default parameters too, like the ones we saw with print() like SEP separator, END line ending. tf 1:33:38

```python
def hello(to="world"):
    print("hello,", to)

name = input("What's your name? ")
hello(name)
```

The function hello takes the parameter "to" and we can assign the the default value of "world" if no argument is given.

tf 1:34:15

### What is main() function?

"Many programming languages have a special function that is automatically executed when an operating system starts to run a program. This function is usually called main() and must have a specific return type and arguments according to the language standard. On the other hand, the Python interpreter executes scripts starting at the top of the file, and there is no specific function that Python automatically executes.

Nevertheless, having a defined starting point for the execution of a program is useful for understanding how a program works. Python programmers have come up with several conventions to define this starting point."

[Link to reference on python main()](https://realpython.com/python-main-function/)

```python
name = input("What's your name? ")
hello(name)


def hello(to="world"):
    print("hello,", to)
```

If we send the function we created at the bottom to be called later it will create an error since is not define, it must already exist so to be read before being called, even if the function is in another file.
tf 1:36:45

So, to not work against continuity, we define the part of the code that is the program itself, the part that call other functions as main. Why the name main?, because is a data convention for this purpose. tf 1:37:30

And at the end we should call the main function, so it can do the work as we intent it to do so. tf 1:38:30

```python
def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()
```

### variable scope

Scope refers to a variable only existing in the context in which we defined it. tf 1:40:23

```python
def main():
    name = input("What's your name? ")
    hello()

def hello():
    print("hello,", name)

main()
```

This will raise an error since name is defined in main() function and not in hello and we are not passing any argument. tf 1:41:33

It is completely up to each individual functions to name its own variables or name its own arguments, but this is a way of handing an argument to a another function the value of that variable. tf 1:40:55

### return keyword

At the moment our Hello function is only showing a side effect, but what if we need the function to return some value, for this the keyword return is use. tf 1:41:13

Most functions have something in common, it return a value. In this case the return keyword allows us that, hand back a value. tf 1:41:30

```python
def main():
    x = int(input("What's x?"))
    print("x squared is", square(x))

def square(n):
    return n * n


main()
```

Or we can use ** that raise the number of the left to the power of the right. tf 1:41:54

```python
def main():
    x = int(input("What's x?"))
    print("x squared is", square(x))

def square(n):
    return n ** 2


main()
```

Or we could use the function called pow, that raise something to the power. It takes two arguments, the fist is the number and the second the exponent. tf 1:45:03

```python
def main():
    x = int(input("What's x?"))
    print("x squared is", square(x))

def square(n):
    return pow(n, 2)

main()
```

### List of topics

1. What is a text editor?
2. What is a code editor?
3. What is an IDE?
4. Why we cannot use rich or enhanced word processing software for coding?
5. How to create a python file in vscode?
6. How to run a python file in vscode?
7. What is python interpreter?
8. What are functions?
9. How helpful is a function?
10. What is an argument?
11. What is a side-effect?
12. What is a bug?
13. What is the print function?
14. What it is input function?
15. What is a return value?
16. What is a variable?
17. What is the assignment operator?
18. What is a comment?
19. What is string?
20. What does the input function expect?
21. How + operator work in Print function?
22. How , separator work in the Print Function?
23. What is the Technical Term for Strings?
24. How can we change a function parameters?
25. How can we change Print function parameters?
26. What is difference between argument and parameter?
27. Types of parameters
    + Positional parameter
    + Named parameters or keyword parameters
    + Default Arguments
    + Arbitrary Arguments
28. How can we use quotes inside quotes?
29. How to format a string in python?
    + f-strings
    + format() method
    + module operator
    + Eager interpolation
    + Lazy interpolation
    + Difference between format methods
30. What are methods in python?
31. What methods can we use with strings?
    + .strip() method
    + .capitalize() method
    + .title() method
    + .split() method
32. What is method chaining?
33. What is the int data type?
34. What types of operators python support?
    + Arithmetic operators
    + Assignment operators
    + Comparison operators
    + Logical operators
    + Identity operators
    + Membership operators
    + Bitwise operators
35. What is interactive mode?
36. How int works?
37. How can we nest functions?
38. What we need to prioritize writing code?
39. What is the float data type?
40. What is the round function?
41. How to change a number to use thousand separator with f-strings?
42. What is float limitations?
43. How to round using round() function?
44. How to round using f-strings?
45. How to define functions?
46. How to define the default parameters of a function?
47. What is main() function?
48. variable scope
49. return keyword.

# Object Oriented Programming

[edx oop link](https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@2e3c5785a8484c8988f8fac546929f35/block-v1:HarvardX+CS50P+Python+type@vertical+block@7878dc1b158f44809ef78d09d9920d71)

## Introduction

There's different paradigms of programming languages, different ways of solving problems with code. With time and
more knowledge we can notice certain patterns, certain capabilities.

## Proceduteral programming

From top to bottom, everyting is step by step, as we expect in general from an algorithm.

## Functional programming

When we start passing functions around, since they work as building blocks, as
anonymous functions, this are features of a functional programming
language. tf 00:1:23

## Object Oriented Programming (OOP)

Is better for longer, larger and more complicated programs.

tf 00:2:42

Example 1a - Proceduteral programming

```python

    name = input("Name: ")
    house = input("House: ")
    print(f"{name} from {house }")


```
Notes:
+ Very simple top to bottom program


Example 1b - Functional programming

```python

    def main():
        name = get_name()
            house = get_house()
            print(f"{name} from {house}")

        def get_name():
            return input("Name: ")


        def get_house():
            return input("House: ")

    if __name__ == "__main__":
        main()

```

Notes:
+ we don't need a variable if we are immediately going to return that
same variable in the next line. tf 00:05:12
+ we keep the habit of including at the end 
    ```if __name__ == "__main__: 
        main()"```
so that, if this eventually becomes part of a module, a librery of sorts,
we don't accidentally call main blindly. tf 00:05:35

Example 1c - Functional programming - tuples

```python

    def main():
        student = get_student()
        print(f"{student[0]} from {student[1]}")


    def get_student():
        name = input("Name: ")
        house = input("House: ")
        return (name, house)


    if __name__ == "__main__":
        main()

```

Notes:
+ we can fuse the two gets in one get_student() function so to retrive
name and house in one single function call.
+ We can return the values in different ways.
    + In python we can return multiple values separated by a ,
        `return name, house`
    + Create a dictionary to create a key/value pair
    + We could return a list.
+ If we utilize the return multiple values, we can unpack them in sequence
like we do with lists. tf 00:09:25
    `name, house = get_student()`
+ This way of returning multiple values, what we are returning is a tuple.
+ A tuple is similar in spirit to a list, but it's immutable. that means
we need to create to store those values in other variables to change it
and store it somewere else, since it's not mutable. tf 00:10:50
+ So what we are returning is actually one value, a tuple.
+ We can use parentesis to be more explecit syntax as im returnin a tuple.
 `return (name, house)`
+ Since we know is a tuple and no need to unpack them there we can store it
in a single variable too like `student`
+ Since a tuple is similar in spirit to a list but inmutable, we can access
them like a list with `[]` starting from 0 index. 
`print(f"{studnt[0]} from {student[1]}")`

Questions:
What's an actual use case of where to use a tuple, list or someting similar?

To program defensively, if we know that the values in this variable shouldn't
change why would you use a data type that allows them to be change?
It invites mistakes, bugs down the line, either by you or collegues who are
interacting with your code.

Tuples is just another way to increase the probability of correctness by not
allowing anyone, including one self to change the contents therein.

Another tool in the toolkit of programming. tf 00:13:50

So if we want it to be mutable we should make it explicit a lists
`[name, house]`

Can we have more tuples inside a tuple?

yes we can or other data types inside as there is no constrain. tf 00:17:56

When we see square brackets, are they mainly use in list?
When we see `()`, it is a tuple when creating
when we see `[]` when creatin we are seeing a list

But when we are accesing an index position, in both we use `[]` to access
the data. `data[0]` tf 00:18:31 
 
Example 1d - Functional programming - using dictionarys

```python

    def main():
        student = get_student()
        if student["name"] == "Padma":
            student["house"] = "Ravenclaw"
        print(f"{student['name']} from {student['house']}")


    def get_student():
        name = input("Name: ")
        house = input("House: ")
        return {"name": name, "house": house}


    if __name__ == "__main__":
        main()

```

Notes:
+ Dictionary is a collection of keys and values, the upside, in particular
is that it have better semantics.
+ We don't need to assume that the values will always have the same position.
+ We don't risk creating buggy code.
+ We cant use double quotes inside double quotes, we can use single quotes inside.
+ Using a dictionary is more expresive, as we don't need to documented who is where.
+ If we are only creating a variable to return it after, we can try to create
the dictionary in the same return statement. This can be good for small scale.
`return {"name: name", "house": house}`
+ Dictionary are mutable as list but using strings as index.

Questions:
Can we change a list inside a tuple?
With list you can change what inside of then after is created since is mutable.
With tuple after is created cannot be change. so is inmutable.

## Classes

With it we can create our own data types and actually give them names.
The terminology is a class.

A class is like a blueprint for pieces of data objects.
A class is like a mold that you can define and give a name.
And when you use that mold or use that blueprint, you get types of data
that are designed exactly as you want.

Classes allow you to invent your own data types in python and give them a
name.

This is a primary feature of object oriented programming, to be able to create
your own objects in this way, in the case of python give them some custom
names. tf 00:28:47

Official url:
docs.python.org/3/tutorial/classes.html

Example 2a - Classes

```python
    class Student():
        ...

    def main():
        student = get_student()
        print(f"{student.name} from {student.house}")


    def get_student():
        print(student)
        student.name = input("Name: ")
        student.house = input("House: ")
        return student


    if __name__ == "__main__":
        main()
```

Notes:
+ We start with the word `class`
+ Class is a general purpose term in a lot of languages, python amond them
that allow us to define these custom containers with custom names for pieces
of data. tf 00:29:39
+  the name of the class by convention start with a Capital letter in this
case S for student. `class Student:`
+ we first create a variable to hold the class student, with a syntax similar
that we use with functions, the difference is that the name of the class
start with capital S. `student = Student()`
+ classes have attributes, properties of sorts that allow us to especify values
inside of them.
+ to access this attributes, we use a dot that is similar in spirit to modules
and l ibraries, that allows us to get at something inside of someting else.
`student.name`
+ we can assign a value to that attribute like with other data types:
`student.name = input("Name: ")`
`student.house = input("House: ")`
+ we then return the variable back `return student`
+ to retrieve this values we simple similar as we use a name in a dictionary to
retrieve a value, we use the name attribute to return the value inside.
`print(f"{student.name} from {student.house}")`
+ Any time we use a class, we are creating an what are called objects. tf 00:33:03
+ when we assign to the student variable the Student() clas, we are technically
creating an object of that class.
+ An object is the incarnatin of, or tecnically instantiation of a class. So another
term for object is instance.
+ the attribute values can be of any data type, for now they are only holding strings.


Questions:
+ Are class objects mutable?
Yes they are indeed mutable, but we can make then inmutable, so we can
have the best of both worlds.

+ What are the properties of those classes?
For now the only attributes are name and house but we can have more down
the line. Attributes are tecnically call instance variables, so name and
house are just variables inside of an object whose type is student.


Example 2a - Classes - Standarized attribute values

```python
class Student():
    def __init__(self, name, house):
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)
    


if __name__ == "__main__":
    main()
```

Notes:
+ Putting manually it's a little reckless of us, classes, unlike dictionarys
allow us to standardize, all the more, what those attribute can be and what
kinds of values we can set them to. tf 00:37:00
`student = Student()`
`student.name = input("Name: ")`
`student.house = input("House: ")`
+ Just by defining a class, you get a function, whose name is identical to the class
name, with the capital letter included. But instead of using open/close parentesis,
we can pass name and house.
`student = Student(name, house)`
+ Standardizing how we pass data into the student class, its going to give us
an oportunity to error check those inputs, to make sure that the name is valid,
that is has a value and it's not just the user hiting enter.
+ In this example allows us to validate house or empty strings. With this
we have more control of the correctness of our data.
+ We have besides instance variables, class methods, that are functions inside
a class. 
+ These class methods, these functions allow us to determine the behavior in a
standard way. They are special methods in that sense.
+ We can define a method inside a class with `def __init__(self):` with it
we can have the oportunity to customize the class's objects.
+ __init__ under score under score is abbreviated Dunder init method and is
specially know as an `instance method`, as python designer definition. So to
initialize the contents  of a object from a class, you define this method.
+ When we used the class Student(name, house) as a function, is generally know as
a constructor call. This line of code infer that is going to construct a student
object for us. Using synonums, is going to instanciate a student object for us.
using the studen class a mold a template.
+ Calling  `Student(name, house)` with arguments inside indicate that there is a 
function somewhere that has been defined `def`, and by definition of how python classes 
work is `__init__` and is what the authors of python chose to implement the 
initialization of an object in python.
+ The self part is a particular weird thing in the init definition.
 `def __ini__(self, name, house)`, like a function since the only two parameter
 that we want are those two.
+ By python authors, we need a third value where to store this values, and there
is where it comes in the self. and we need to define it first. We can call it werever
we want, but by convention is called self. An as the name implies, give us access 
to the current object that was just created.

Questions:

What is the difference between init method and default constructor?

+ For instance, java there are functions that are explicitly called 
constructors that construct an object. They inialize it with values.
Python tecnically calls this init method the initialization method.
It initializes the value. There is another method called __new__ that
creates an object but for us with __init__ would sufise leaving to python
create the object for us and initialize for us.     


What if we want to store more than one name?

+ We can create something like self.names equal to a list of names


Where are store in memory those objects?

+ The objects are represented by certain quantity of bytes, in certain place
in memory, we as programmers we deal with logic and python deals with the
low level part of where to store the object.                                                                                                                                                                          


Why use classes instead of dictionarys?

+ We can ensure the correctness of your data much more with classes
+ Error check
+ We can design more complicated software more effecively.


## class encapsulation of functionalitys

In object oriented programming, encourages us to encapsulate, inside of a
class, all the functionality related to that class.
So if we want to validate that a name exist, validate houses. we have all this
that belongs to the student inself inside the class and not some random function
wrote elsewere. tf 00:52:09
All this is methodology but as program gets bigger is convenient to keep all
the of the name and all the house related code in the student for better
organization and keeping all of the related code together, set you up to
success down the line.

Example 3a - encapsulate functionalitys - error check

```python
    class Student():
        def __init__(self, name, house):
            if not name:
                raise ValueError("Missing name")
            if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
                raise ValueError("Invalid house")
            self.name = name
            self.house = house


    def main():
        student = get_student()
        print(f"{student.name} from {student.house}")


    def get_student():
        name = input("Name: ")
        house = input("House: ")
        return Student(name, house)

    if __name__ == "__main__":
        main()
```

Notes:
+ we can do error check in our class, since is not good to have an object
with error values.
+ in the class Student we can do an `if not name` to check if name is not
empty, and we need to do it in a way that won't close all the program for
this alone. So sys.exit() wont be a good solution, nor return None since
the object is already created.
+ We can raise errors to catch errors and handle them in a way that won't
quit the whole program.
+ We can in the case of the if, we can raise ValueError and treat the
ValueError as a function and pass them an explanatory message that as of
why this error happended.
```
    if not name
        raise ValueError("Missing name")
```
+ if we create an if to handle houses like:
```
if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
    raise ValueError("Invalid house")
```
This show us a pretty solid difference between a class and a dictionary,
with the dictionary, it will go inside no matter what, if is empty or bad
value, but with a class and by way of the init method, we can now control
exactly whats going to be installed inside of the object, and more control
over correctness. tf 00:58:22

Questions:
What if the student have a name, middle name and last name?
+ Yes we can,  the class allows us to create more attributes, we can even
take a list of attributes, but we need to select a way to implement it
and create more validations for each attribute.

Can we import the class for other projects?
+ Yes, not just student, but others too, you can create your own library of
classes by putting the student class in your own module or package.

Can you have optional variable in classes and if you can have your own error names?
+ yes, we can default the parameter to equal None in the init function.
and for own error names, yes you can and there is a suit of exceptions that exist.


Example 3b - encapsulate functionalitys - printing the student

```python

    class Student():
        def __init__(self, name, house):
            if not name:
                raise ValueError("Missing name")
            if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
                raise ValueError("Invalid house")
            self.name = name
            self.house = house
            
        def __str__(self):
            return f"{self.name} from {self.house}"


    def main():
        student = get_student()
        print(student)


    def get_student():
        name = input("Name: ")
        house = input("House: ")
        return Student(name, house)

    if __name__ == "__main__":
        main()

```


Notes:
+ If we to print the contents of student object by eliminating 
`print(f"{student.name} from {student.house}")` and only leaving instead 
`print(student)` we will not see the information inside the student object,
instead we only see where is store in memory like:
 `<__main__.Student object at 0x70bbfbf304a0>`
But we can override this as well.
+ there is another special class method `__str__` that we define inside our
class, that python automatically call this function if another function
wants to see the object as a string. So by default if we dont have this
only the memory allocation would be see.
+ `__str__` only takes one argument `self` when define, so that you access
to it.
+ bellow we a return string.
+  With the self argument it will always be passed a reference to the current student object.
+ the return string, can have access to the values store in self.name self.house from `__init__`
resulting in `return f"{self.name} from {self.house}"`

Questions:
Is there anything else that the underscore underscore str method can do?
There are many methods that come with python classes that start with __

What is the difference between str an repr?
+ `__repr__` Is a representation of the python object meant for developers'eyes
+ it typically has more information than "Harry from Gryffindor"
+ it would indicate what type of object it is.
+ str method is more for use as user friendly.
+ Both str and repr can be overriden as you see fit.


Example 3c - encapsulate functionalitys - creating our own  custom class methods.

```python

    class Student():
        def __init__(self, name, house, patronus):
            if not name:
                raise ValueError("Missing name")
            if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
                raise ValueError("Invalid house")
            self.name = name
            self.house = house
            self.patronus = patronus
            
        def __str__(self):
            return f"{self.name} from {self.house}"
        
        def charm(self):
            match self.patronus:
                case "Stag":
                    return "🦌"
                case "Otter":
                    return "🦦"
                case "Jack Russel terrier":
                    return "🐶"
                case _:
                    return "🪄"


    def main():
        student = get_student()
        print("Expecto Pratonus")
        print(student.charm())


    def get_student():
        name = input("Name: ")
        house = input("House: ")
        patronus = input("Patronus: ")
        return Student(name, house, patronus)


    if __name__ == "__main__":
        main()

```

notes:
+ we add an additional parameter `patronus` but witout error checking.
+ Whats powerful about classes, unlike dictionaries alone is that classes
can have, not just variables or instance variables, they can also have
functions built in, aka methods.
+ When a function is inside a class, it's called a method, but it's still
a function.
+ `__init__` and `__str__` are special methods, that if we define then, they
just work, python automatically call them for you.
+ If we want to represent more real world functionality to our class, we
can create a function inside a the class that we can call.
+ we can def the function like other functions but, because is a method
inside a class, the convention is that it's always going to take at least
one argument, called self, by convention so that you have access to the
current object, even if you don't plant to use it, per se.
`def charm(self)`
+ We define inside the charm function, a `match self.patronus` where each
case is a string of each know patronus.

tf 01:15:35

Questions

Can we call the method outside the function?
+ Yes we can, like with methods for strings like split or others methods
+ The difference with init and str methods is that python will call them
automatically when you try to create a student or when we try to print a
student respectively.
+ We use the dot to denotate that the method is inside the class object.
and we can get access to it like with instance variables like:
`student.charm()`

Why did you use self in the charm function?
+ all methods and functions that correspond to that class is indented bellow
it.
+ init, str, charm methods are all inside or part of that class 
+ by convention the methods inside the class should expect that python will
automatically pass in at less one argument to every method in that class
and that argumento will always be a reference to the current object, the self
+ class method are define inside the class, so self makes reference to the
object.
+ appart from self, they can be 0 or more arguments that is up to use to declare.

How are printed emoji with double quote in the python?
+ an Emoji is just a character, its part of a mapping of numbers to letters 
know as Unicode.
+ When we see an emoji, we only type characters, that represent in Unicode an image.
+ So when we send the emoji to print, we are sending an unicode code that will
be represented as an image.

## Making our class more robust
+ We  can circunvent the init validations after the item is created, this is resul
becuase the validations on the init are only run when creating the object.
+ It doesn't necessarily prevent the user be it rather the programmer, a collegue
from messing things up.
+ To be more defensively to this case, there is another feature in python namely
`properties`

## Properties
+ Is an attribute that has even more defense mechanisms put into place by you
to prevent programmers to mess things up.
+ How we do this, we just write a little more code using some python conventions
like the feature `@property` which is technically a function property

## Decorators
+ It allows you to decorate functions and this is a term of Art in the world of
python.
+ Decorators are functions that modify the behavior of other functions functions
+ With decorators we can define properties.

## Getter
+ Is a function for a class that gets some attribute.

## Setter
+ Is a function in some class that set some value


Example 4a - Properties and Decorators - Getter and Setter

```python

    class Student():
        def __init__(self, name, house):
            self.name = name
            self.house = house
            
        def __str__(self):
            return f"{self.name} from {self.house}"
        
        @property
        def name(self):
            return self._name
        
        @name.setter
        def name(self, name):
            if not name:
                raise ValueError("Missing name")
            self._name = name
        
        @property
        def house(self):
            return self._house
        
        @house.setter
        def house(self, house):
            if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
                raise ValueError("Invalid house")
            self._house = house


    def main():
        student = get_student()
        print(student)
       


    def get_student():
        name = input("Name: ")
        house = input("House: ")
        return Student(name, house)


    if __name__ == "__main__":
        main()


```

Notes:
+ We create our setter that is a function for a class that gets some attribute.
and the getter that is a function in some class that set some value.
```
    # Getter
    def house(self):
        return self.house
    
    # Setter
    def house(self):
        self.house = house

```
+ With this we are trying to prevent programmers are ourself from circumventing
our error checking that we put in place in the init.
+ We have in programming, variables for data and functions for actions, so
to do the prevention, we somehow require that in order to access an attribute, you
go through some function, and in order to set some attribute you go though some function,
by convention they are called getter and setter.
+ We can in our setter function implement our validator code, effecively raising an value error
if the data is not in our list of valid houses.
+ When we try to change the value of an attribute, python will automatically check for `self.house`
in this case the function in the class when we type something like `student.house = "Number four, Privet Drive"`
where it will know that we are trying to set with the equal sign a value to `self.house` and automatically 
run the setter function, plus run the validating, effecively raising an error if the value is not true.
+ for indicating to the class that the next funtion is a getter with place on top of it the keyword
`@property`.
+ for indicating that the next function is a setter we define the keyword like:
`@house.setter` where house is the attribute to set.
+ for convention the functions name should be the name of the attribute that they
want to  change
+ the getter will only take 1 argument self, but setter gets 2 arguments, one self and the
second argument from the programmer.
+ When we do the `self.house = value` inside or outside the class function
python will automatically call the setter method, this way we can set the validations
there and it will always make the validations for us, making our code more robuts.
+ Setter will be called anytime we access .house
+ Lastly, we need to fix the collided names, we cannot have our instance variables
or our functions with the same names, they are gonna collide, so one of the two
need to have a different name. By convention in the self.house inside the function house
we add an undercore _ in front the instance variable name like: 
`return self._house`. This apply to the getter and setter.
+ This way of placing the error check in the setter to code defensively, makes
a better design.

Questions:

Why are we defining getter and setter?
+ Because we want to make sure that programmers cannot change things that
don't supose to do, not creating bugs later on.

When we use getters we just have one argument and setter have two arguments?
+ getter always get the self value, and setter always is self and other value,
becuase that is his role to change something for that other value we provide.

Why din't we use the _house in the init method too?
+ We want for python to recognise the pattern of `self.house =` the . + = will automatically
call the setter even if we are passing the house via Init method.
+ If we place the self._house in the ini method, it will circumvent the 
setter and now there is no error check.


## Python focus in conventions not hard constrains

In python focus in conventions because it allows for example to use ._ instance
variable in the main function like `student._house = "Number Four, Privet Drive"`
and unfurtanaly circunvent the error checks and allow the change.

In languages like Java that just prevent you from doing things like this,
java itself allows you to specify that certain instance variables are public,
accessible to anyone in the code, private or protected. In the world of python
there is only the honor system, by convention if you see a instance variable that
start with _ , please dont touch it.

## int class
Since the start we are using classes, functions and methods
per documentation when we use int function we obtain an object of class int

class int(x, base=10)

## str class
Since the start have been classes as well, where per documentation is like
this: class str(object='') where when we create an string we obtain an object
of type string. Anytime we use str.lower(), we are calling a method called lower()
that is inside an class object type str that will return an object that contains
a string in lowercase.

## list class
Since the start list is a class: `class list([iterable])`
methods: list.append(x) append to the current list etc.

## dict class
The dict () function can be used in the following formats.

+ class dict (**kwarg)
+ class dict (mapping, **kwarg)
+ class dict (iterable, **kwarg)

## Build in classes
Most of the classes we use that come with python, are tecnically lower case, 
even tho we know classes should they should start with a capital letter by
convention, but in python their build-in data types, even that they are classes
they start with lowercase.

Where a list can be `[]` or `list()` and dictionarys can be `{}`  `dict()`
like: list, int, str, dict

## Other type of variable and methods:

## class methods
Is when you want some functionality, some action to associated with the class
itself no matter what the specific objects own values or instance variables are,
and for that we have the keywork `@classmethod` that is another decorator, another
function that specify that this method is not by default implicitly an instance
method that has access to self the object itself, but it does know what class is
inside.

Example 5a - classmethod - sorting hat - bad design

```python

    import random

    class Hat:
        def __init__(self):
            self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

        def sort(self, name):
            print(name, "is in", random.choice(self.houses))
            

    def main():
        hat = Hat()
        hat.sort("Harry")


    if __name__ == "__main__":
        main()

```

 Notes:
+ We first define the `class Hat:` with ... three dots as placeholders
 so as to build later.
+ We then start creating our code using the class, thinking we already
 have that functionality.
+ we create a variable hat that will hold the hat object `hat = Hat()`
+ Since is a sorting hat, we can use a class method called sort.
`hat.sort("Harry")` and should say what house the student is.
+ since we need a sort function we start with that inside the hat class.
+ we define the function method inside a class with two arguments even if
outside takes one, since we always need to add self plus the argument
`def sort(self, name)`
+ we create a init method that only takes self, since our Hat() wont take
arguments `def __init__(self):`
+ then we create a instance variable named haouses that for now contains
a list of houses. `self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]`
+ since self.houses is define at the very top, in the ini method it give access to the whole class.
+ inside the sort since we are print an string, we could use the ramdom.choise method to give
ramdomnes. `print(name, "is in", ramdom.choise(self.houses))`
+ So that the ramdom function to work, we need to import his library. `import ramdom`
+ When you should use a class to represent something in your code, very often when
you're trying to represent some real world entity or fantasy world entity, like a 
student, something from the realworld or a sorting hat from a fantasy world.

## The real sorting hat

In the world of harry potter there is only one sorting hat, but here
we implemented a sorting hat. A class is like a blueprint, a template, a
mold that allows you to create one or more objects thereof.
So for the sorting hat or realworld student, there is really one, one
Singleton wich is a term of Art and a lot of context of programming.

Example 5b - classmethod - sorting hat - improve design

```python

import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))
        

def main():
    Hat.sort("Harry")

if __name__ == "__main__":
    main()

```

Notes:
+ We don't have to instanciate a Sorting hat `hat = Hat()`. we just need
to represent the Sorting Hat with a class, because it already exist, we
just need one.
+ Up util now we have been creating instance methods, functions inside
classes that are automatically passed a reference to self, the current objet,
but sometimes you dont need that, sometimes it just suffices you just to know
what the class is and assume that there  might not even be any objects of that
class so in this sense you can use a class really as a container for data
and or functionality that is just somehow conceptually related things related
to a Sorting Hat and there is this other decorator or function called 
@classmethod that allows us just that.
+ if we are not initialize, we dont need __init__ method, since is for 
initialize specific objects from that blueprint that template that mold.
+ if we dont have init method we dont have access to self, but is ok
+ in Classes we have class variables and class variables exist within the
class itself and there is only one copy of that variable for all of the objects
thereof, they all share if you will the same variable, be an int, str, or a list.
+ so we define a class variable witout self inside class:
`houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]`
+ since is inside the class function, it is accesible to all the methods
inside the class.
+ So to specify that there would be only one sort in the sorting hat
we use the decorator  `@classmethod` before the sort definition and since
we are not passing self, by convention we pass a reference to the class
inself with `cls` cls for class short since we cant use the same phrase
as class, it will conflict with the class keyword.
```
@classmethod
def sort(cls, name):
    print(name, "is in", random.choice(cls.houses))
```
+ So at the moment we can delete the instantiation of hat `hat = Hat()`
and directly use the class and class method `Hat.sort("Harry")`
+ the difference between instance method and classmethod with decorators
is that instance method is not define with @classmethod so it will be
considered instance method witout it.

Questions:
Can you define a class inside another class?
+ You can Define one class inside another class, but generally this is not
done, but there maybe are cases where it maybe helpful especially for
larger more sophisticated programs.

What about the self.houses, why we remove the self?
+ When we are creating an object, the way to access the data specific to that
object is by using the self in the init dunder `__init__` method.
So for instances self.houses would be an instance variable.
+ When we only want it to be a container and dont bother to create instances
or want to use the functionality witout create an specific object we 
create a classmethod.

What is the difference between class hat and a function?
+ Putting apart the better design, abstraction and security, both ways
could work.
+ With object oriented programming is just a different way of modeling the
world, so depending on the complexity of the programm, oop will do better for
larger, more complex and sophisticated programms.
+ It will organize the functions, group them together if they are related,
so to keep our world in order.
+ Object Oriented programming is just a way of encapsulating related data
that is variables, related functionality that is methods inside things that
have names, these things are called classes. It's just another way to solve problems
like librarys.
+ Which one you  should use overlaps, if you are familiar with venn diagrams
the overlaping regions mean you could use a class or you could use a module or 
a package or you could use a single local file, with time you develop an instinc,
a personal preference for which tool to use.

Example 6a - clean up student.py with @classmethod

```python

    class Student():
        def __init__(self, name, house):
            self.name = name
            self.house = house
            
        def __str__(self):
            return f"{self.name} from {self.house}"
        
        @classmethod
        def get(cls):
            name = input("Name: ")
            house = input("House: ")
            return cls(name, house)


    def main():
        student = Student.get()
        print(student)
       

    if __name__ == "__main__":
        main()

```


Notes:
+ first we simplify eliminating the properties (getter and setter) so to
focus in the ideas of classmethod.
+ the function get_student was a miss oportunity to clean up our code, why
if we have a class name student, you a collegue or other programmers will
asume that everyting related to student is bundled up encapsulated inside
of the student class, then it will confuse everyone if there is a function
related to student outside in the code.
+ the get_student works as is intended, ask user for inputs for name and house of
student then pass this information to the Student class as arguments, returning 
the instance student object to a variable elsewere.
+ When the code gets more complicated, larger and sophisticated, it would not
be ideal to have the get_student functionality elsewere that its not in the student class
inself.
+ This is evidence of bad design, not for short programs, but this is an example of code smell.
That smell like something smells a little of here, and probabily with get us in trouble
later by separating related functionality.
+ So we eliminate get_student and in the class student we define get method
like `def get(cls):` this means get() function will take one sole argument, by
convention is `cls` that means the class inself, then we create input name and house
and lastly return a new student object by calling class constructor and pass 
name and house `cls(name, house)`, this means create an object of the current
class.
+ lastly we use the decorator @classmethod above the get function, this
indicate that the function is a classmethod, where it just mean we can 
call this method witout instanciating a student object, solving the problem
of the chicken and the egg (who go first).
```
@classmethod
def get(cls):
    name = input("Name: ")
    house = input("House: ")
    return cls(name, house)
```
+ `cls(name, house)` is a reference to the class student inself, where init method
of the class student takes two arguments, and `self` needs to be there by default.
+ then we can change in main the get_student for `student = Student.get()` where
should call the classmethod get, ask for name and house and create an instance
object of that class.

Questions:
Does the class needs to be define before the main function, in terms of the
order of the program?
+ When in doubt try to do it.
+ In this it does not matter because we are not calling main, in the begining
only at then, after everyting have been read, top to bottom, left to right.
+ Generally main is define at the top of the file.
+ It could be cleaner if we move the classes definitions to its own file and
then import it, so enssentially to make reusable code.

Is there a way to declare all the possible attributes of the class, since looks
very inconsistent?
+ Java and other languages have ways to do that, but in python community choose to
implement this idea.
+ The right mental model that these instance variables, instance methods belong to
or operate on specific objects a specific student a specific hat, class variables
and class methods operate on the entire class itself or in turn all objects of that
class.

## static methods
static methods use a decorator like `@staticmethod`

search more information on this topic...


## inheritance

Is one of the most compelling features of object oriented programming
where you design your classes in a hierarchical fashion whereby you can
have one class inheri from or borrow attributes that is methods or variables
from another class if they all have those in common.

Example 7a - inheritance

```python

    class Wizard():
        def __init__(self, name):
            if not name:
                raise ValueError("Missing Name")
            self.name = name

        def __str__(self):
                return f"{self.name}"

    class Student(Wizard):
        def __init__(self, name, house):
            super().__init__(name)
            self.house = house
        
        def __str__(self):
            return f"{super().__str__()} from {self.house}"

    class Proffesor(Wizard):
        def __init__(self, name, subject):
            super().__init__(name)
            self.subject = subject

        def __str__(self):
            return f"{super().__str__()} impart {self.subject}"

    wizard = Wizard("Albus")
    student = Student("Harry", "Gryffindor")
    proffesor = Proffesor("Severus", "Defense Aganist the Dark Arts")

    print(wizard)
    print(student)
    print(proffesor)

```


Notes:
+ We start defining our classes one for student and one for professor
each one with an init method, self, name variable, where in student the last
attribute is house and proffesor is subjet.
+ With only this we start to see a pattern that is repeating itself, even more
if we create error checking for example the same attribute name, where we should
have the same error check in both classes, there is where the red flags should
start sound, since if we need to copy paste the same code in several parts,
there should be a better way to do this.
+ oop offer the solution to have to reuse code, inheritance where you can define
multiple classes that somehow relate to one another, where they don't have to exist
in parallel, there could actually be some hierarchy between them.
+ We need to create a third class where we can factor out those common points.
In this case creating a class wizard that will have those attributes or methods inside.
+ We can now eliminate the redundant code of the other classes.
+ We need now to link these together and the way we can prescribe inheritance, whereby
one class should inherit from another or conversely one class should descend from another.
We do this by declaring the wizard before the `:` and we could go and say in parentheses a
student inherits from or is a subclass of Wizard `class Student(Wizard):` wich conversely
is the superclass of the student class.
+ This means when we define a student class, go ahead and inherit all of the 
characteristics of a wizard aswell.
+ We can do the same for professor, but since each of them have a init method, and we need
to init wizard class, we can do this with the super() method, that makes reference
to the superclass, in this case wizard, then call the init method of the superclass 
where we pass student name attribute. `super().__init__(name)` and this can be safe
to do in both student and proffesor since error check is in wizard.
+ super() is a way of programmatically a current classes parent class or super class.
+ __init__ refers to the super class init method.
+ wizard = Wizard("Albus") creates an object of class wizard that only contains a name.
+ student = Student("Harry", "Gryffindor") creates an object student that
will call the init of the student class and in turn call the init method of
the super class wizard will be call.
+ professor = Proffesor("Severus", "Defense Aganist the Dark Arts") creates
an object proffesor that will call the init method of proffesor class and
in turn call the super class wizard init method will be call too.

Questions:
Can you nested inheritance?
Yes you can, as we have traits from great granfather, grampa, parents, we too
can inherit functionality from a hirerarchy above.

Can you have like two parents on the same level?
Yes, there are ways to implement decendants from multiple parents and there
is different ways to do this in python and many other languages.

Can we have more attributes in the super().__init__(name)?
Yes, but it depends of how many attributes it is expecting, in this case
it is only expecting one attribute that is name.

## Best example of hirarchy in inheritance exceptions
from per  documentation there are many types of exceptions, but
all decent from a parent class, and many of the subclass have they own
subclass.
So if you want to create your own exception, you can enherit from a
related excentions functionality and add your own twist.


## operator overloading

Python and other languages support this notion of operator overloading,
whereby you can take very common symbols like plus or minus or other such
syntax from the keyword and you can implement your own interpretation.
for example + is not only sum two int or float values, it too can be use
to concatente strings, so python authors have overload the + symbol for 
addition but with different data types to solve slightly diffent problems.

Creating a vault of a bank in Wizardly world.

Example 8a - operator overloading

```python

    class Vault():
        def __init__(self, galleons, sickles, knuts):
            self.galleons = galleons
            self.sickles = sickles
            self.knuts = knuts
        
        def __str__(self):
            return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"


    def main():
        potter = Vault(100, 50, 25)
        print(potter)

        weasley = Vault(25, 50, 100)
        print(weasley)

    if __name__ == "__main__":
        main()

```

Notes:
+ first creating the `class Vault`, a vault another real world or fantasy world entity
that we want to represent with code. We could use a tuple or a list or dictionaries but
we are gonna get a lot more of functionalitys with classes and operator overloading.
+ second we define the init method, with three attributes galleons, sickles, knuts, of course the default self cannot be
omitted, where these attributes would have default arguments of integer 0.
`def __init__(self, galleons=0, sickles=0, knuts=0)`
+ thierd, we define the instances variables that refers to an attribute of the 
instance being created or modified. where `self` allows each instance of class to
maintain its own separate values for these attributes.
```
self.galleons = galleons
self.sickles = sickles
self.knuts = knuts
```
+ There could be error check, if the values or no values are integers or empty inputs,
but for now is good build practice to focus in the idea first then refine later.
+ fourth, if we want to print the instance variables data, we need to define the
str method, so we can return a string cotaining the information we want to show
at the moment of print.
```
def __str__(self):
    return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"
```
+ we can create then two instance object, on vault for potter and other for weasley,
where we pass values to the class contructor for each galleon, sickle, and knuts.
```
potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)
```

What if we want to combine Vaults money?

Example 8b - operator overloading - Combining Vaults information simple way

```python

    class Vault():
        def __init__(self, galleons, sickles, knuts):
            self.galleons = galleons
            self.sickles = sickles
            self.knuts = knuts
        
        def __str__(self):
            return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def main():
        potter = Vault(100, 50, 25)
        print(potter)

        weasley = Vault(25, 50, 100)
        print(weasley)

        galleons = potter.galleons + weasley.galleons
        sickles = potter.sickles + weasley.sickles
        knuts = potter.knuts + weasley.knuts
        
        total = Vault(galleons, sickles, knuts)
        print(total)

    if __name__ == "__main__":
        main()

```

Notes:
+ we in this case created variables that will hold the sum of the values
of each intance variable of each object. Then with that sum we created a 
new instance vault object with the sum of the two, then print.
+ This aproach is tiresome since we created manually variables, made the
math, asign an created a new object to show the results, there is a better
way for this.


Example 8c - operator overloading - Combining Vaults information - operator
overloading way

```python

    class Vault():
        def __init__(self, galleons, sickles, knuts):
            self.galleons = galleons
            self.sickles = sickles
            self.knuts = knuts

        def __str__(self):
            return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

        def __add__(self, other):
            galleons = self.galleons + other.galleons
            sickles = self.sickles + other.sickles
            knuts = self.knuts  + other.knuts
            return Vault(galleons, sickles, knuts)


    def main():
        potter = Vault(100, 50, 25)
        print(potter)

        weasley = Vault(25, 50, 100)
        print(weasley)

        total = potter + weasley
        print(total)


    if __name__ == "__main__":
        main()

```

Notes:
+ In this case, we could overload the + operator to simple do
`total = potter + weasley` taking out previous declarations. Like str does,
list does.
+ the documentation for this:
docs.python.org/3/reference/datamodel.html#special-method-names
where we have this: `object.__add__(self, other)`
+ This works for any object, be a vault or str or a list or something elsewere
by convention, the add method will take by convention first self then second
by convention other object. where self and other will work as  self + other.
current object + other object. we could call other someting else, but we
should follow conventions.
+ We define then inside our class the __add__ method, where we overload
the plus operator in a way that when it see two objects of the same class
with a + in the middle will try to call the __add__ method.
`def __add__(self, other):`
+ Where outside the class when we do `total = potter + weasley`it will send
two arguments, whatever the operand is on the left in this case potter and
whatever the operand to the right in this case weasley.
case.  where they will be pass as self, and 
other respectively.
+ inside the add method we define the logic of the sum, where we create
variables that will hold the sum of the `self` gallenos, sickles and knuts
to the `other` galleons, sickles and knuts then lastly return a new 
instance vault object with the variables  of the sum of each currency.
```
def __add__(self, other):
    galleons = self.galleons + other.galleons
    sickles = self.sickles + other.sickles
    nuts = self.knuts  + other.knuts
    return Vault(galleons, sickles, knuts)
    
```
+ this way we teach python, what it means to add two vaults together.

Questions:
How would you go about creating a function for adding a student and a vault
for two separated class?
Yes, but depends much of the type of values you are trying to add
so for potter + str() generates a attribute error because the adding
was define for expecting an integer, but depending of the outcome
we are looking we can  build something that can work that out.

Can you define new operators in python?
+ No, there is a long pricise list of operators that you can overload,
you cant assign arbitrary character to be operators in python.

The only operator you can do this with substraction too?
Yes, with substraction and many others as per documentation.

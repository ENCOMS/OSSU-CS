# classes

Example 1a - classes

```python

class Package():
    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight

    def __str__(self):
        return f"Package number: {self.number}, sender: {self.sender}, recipient: {self.recipient}, weight: {self.weight}"

def main():
    packages = [
    Package(number=1, sender="Alice", recipient="Bob", weight=10),
    Package(number=2, sender="Bob", recipient="Charlie", weight=5)
          ]
    print(packages[0])
    print(packages[1])

if __name__ == "__main__":
    main()

```

notes:
+ we have a packages a list of two dictionary, two packages
+ string are flexible, maybe too flexible.
+ if we want something more ridgit for our information, thats where classes
comes in.
+ classes operates like a template, that we can use to create  various objects
in code.
+ we can think as each package as an object, literally from real world.
+ for this we need to identify some pieces of information we want this packages
to encapsulate, for example the id of the packages, store the sender and
recipient of the packages, alongsi de the weight as well.
+ classes allows us to encapsulate this information in a single place
aka related information.
+ we start creating a class with class + name of the class
`class Package:`
+ we then inside we need to first create this particular method called
dunder init or __init__ method. Which allows us to use the template, our
class, to instantiate or create some particular object from this template.
`def __init__(self):`
+ the dunder init takes by convention at least one argument or attribute,
called self, self makes reference to the object to instantiate or created
from this template.
+ so in this case a we need to encapsulate the package information in the
init method. `def __init__(self, number, sender, recipient, weight):`
+ the self will indicate the current instance object, so we can try to 
assign to this new instance of our object, everyting we have passed in down bellow.
creting in this case instance variables.
```
self.number = number
self.sender = sender
self.recipient  = recipient
self.weight = weight
```
+ in the main, we can use `Package()` constructor, where we are actually calling
our dunder init method, to create some new instance of the template.
`packages = [ Package() ]`
+ now we can fill the information, creating as packages as we need.
```
packages = [
    Package(number=1, sender="Alice", recipient="Bob", weight=10)
    Package(number=2, sender="Bob", recipient="Charlie", weight=5)
          ]
```
+ we can add a str dunder to print the information of the instance package object.
```
def __str__(self):
    return f"Package number: {self.number}, sender: {self.sender}, recipient: {self.recipient}, weight: {self.weight}"

```


# instance variables
+ In this package example before, we created a class, a template a mold,
then later down bellow, we  define two instances of this class that we
called package. So we create a template and later we created a particular
package with contents in it.
+ When we invoke the class Package() we call this method called dunder init
that take as input at least one argument called self, and other we can define
if needed.
+ in the dunder init, we define apart from the self, 4 more inputs and
assigning them to various attributes or properties of this class. Whenever
 we call the Package() it define the attributes of that instance object. 
+ An attribute or propertie of class is a variable that is bound to an
instance the class, aka a new object of the class. An attribute is typed as
`self.number` and we can call them `instance variables`
+ For short, with self.number we are accessing a variable called number
that is inside a instance object.

Looping each of the packages

Example 1b - Instance variables

```python

    class Package():
        def __init__(self, number, sender, recipient, weight):
            self.number = number
            self.sender = sender
            self.recipient = recipient
            self.weight = weight

    def main():
        packages = [
        Package(number=1, sender="Alice", recipient="Bob", weight=10),
        Package(number=2, sender="Bob", recipient="Charlie", weight=5)
              ]
        
        for package in packages:
            print(f"Package {package.number}")

    if __name__ == "__main__":
        main()

```

Notes:
+ So we want to loop the contents of the list of packages to check the contents.
For that we create a for loop so as to access each item inside the list.
`for package in packages`
+ In a simple way we can access a instance variable, refering to the instance of
the class, followed by a dot, followed by the instance variable's name.
`package.number` where package will hold any of the two packages.


# instance methods
+ We can use classes not to just encapsulate or combine pieces of information
but also encapsulate functionality that you want to be common across all
individual packages. And we can do this by defining a instance method.
+ An instance method is a particular kind of function that is part of a class.
that can be use by any instance of this particular class.
+ dunder str method is a particular function that can be called to print
some package information.
+ If we try to print a package witout the str method define, we obtain
the address on memory of the instance of class.
+ dunder str or `__str__` are part of the special functions that python have.
in this case python attach the meaning that dunder str will be called
everytime we want to print the instance of our individual package.


Example 1c - instance methods

```python
    class Package():
        def __init__(self, number, sender, recipient, weight):
            self.number = number
            self.sender = sender
            self.recipient = recipient
            self.weight = weight

        def __str__(self):
            return f"Package {self.number}: {self.sender} to {self.recipient}, {self.weight}kg"

        def calculate_cost(self, cost_per_kg):
            return self.weight * cost_per_kg

    def main():
        packages = [
        Package(number=1, sender="Alice", recipient="Bob", weight=10),
        Package(number=2, sender="Bob", recipient="Charlie", weight=5)
              ]
        
        for package in packages:
            print(f"{package} costs ${package.calculate_cost(cost_per_kg=2)}")

    if __name__ == "__main__":
        main()
```

Notes:
+ when we define dunder str method, it takes as input the instance of the class
itself, that we refer as `self` like: `def __str__(self):`
+ then we return the string to be printed everytime we print a package.
+ to access the information of the instance variables, we use the same
syntax as in init to refer to the instance variable, `self.number`
+ so the return can look like this:
```
def __str__(self):
    print(f"Package {package.number}: {package.sender} to {package.recipient}, {package.weight}kg")
```
+ we can create a function inside the class, called calculate_cost, where it
takes self as first argument refering to the instance of the class, and a
second argument, the cost. `def calculate_cost(self, cost_per_kg)`
+ inside we can define that the instance varible self.weight would be multiply
by the variable cost_per_kg. `return self.weight * cost_per_kg` this asuming the
user knows that is in kg.
+ then in the main function we could print the package information and the cost.
where we declare the package followed by a dot then the instance method name
then followed by parenthesis where we indicate the cost_per_kg in integer.
```
for package in packages:
        print(f"{package} costs ${package.calculate_cost(cost_per_kg=2)}")
```


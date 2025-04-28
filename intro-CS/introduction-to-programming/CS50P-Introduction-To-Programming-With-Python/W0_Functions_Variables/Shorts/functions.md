# Functions

## [Link to short on Functions](https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@744dad66fcce478a92fb1073b3d373fa/block-v1:HarvardX+CS50P+Python+type@vertical+block@085ac859b4024776ae5a5c49d9ba6dc9)

### What is a function?

Is some piece of code that takes an input and produces some output. tf 0:36

One function build into Python is called print() function. tf 0:58

### What is the print function?

Is a function build into Python where the print function takes some text as input and produces as output as text in the terminal window. tf 1:10

```python
print("Hello, world!")
print("This is CS50P.")
```

```console
Hello, world!
This is CS50P.
```

### How can be identify a function?

Function have identifiers we can use to determine when we are looking at a function.

```print("Hello, world!")```

+ It have a name "print"
+ It have parentheses.
+ It may have some input or nothing at all

tf 2:45

### What are custom functions

Are functions we create to solve a particular problem that a default function can't.

For creating a function we use the DEF keyword that stand for define. tf 3:08

```python
def main():
....
```

Everything that will run on that function should be indented after creating the function. tf 3:43

```python
def main():
    print("Hello, world!")
    print("This is CS50P.")
```

### Default functions

Are functions the Python developers defined elsewhere in the Python library like print. tf 4:31

### Python don't auto execute functions in this case main

We have created main function, but we have not called it yet in the code. tf 5:55

```python
def main():
    print("Hello, world!")
    print("This is CS50P.")

main()
```

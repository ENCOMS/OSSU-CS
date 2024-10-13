# Return Values

## [Link for CS50P short about return value](https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@744dad66fcce478a92fb1073b3d373fa/block-v1:HarvardX+CS50P+Python+type@vertical+block@085ac859b4024776ae5a5c49d9ba6dc9)

### Functions outputs

Functions are the building blocks of programs that take input and produce output. tf 0:11

They can produce two kinds of outputs:

1. side effects
2. return value

tf 0:27

### Side-effect

A side effect is something observable from outside the function other than returning a value. So if your function modifies a pass-by-value variable, that is a side effect; if it writes to disk, that is a side effect; if it calls a restful api, that is a side effect.

[Link for reference on return value in stackoverflow](https://stackoverflow.com/questions/67091347/understanding-functional-programming-side-effect)

### Example of side-effect

```python
def greet(input):
    if "hello" in input:
        print("hello, there")
    else:
        print("I'm not sure what you mean")

greet("hello, computer")
```

### return statement

A return value is some value a function can pass to a program to use later on in the code. tf 1:40

If we want to use the return value, we need to capture it or using it on a program. tf 2:38

"A return statement is used to end the execution of the function call and “returns” the result (value of the expression following the return keyword) to the caller. The statements after the return statements are not executed.

If the return statement is without any expression, then the special value None is returned. A return statement is overall used to invoke a function so that the passed statements can be executed."

```Note:``` Return statement can not be used outside the function.

[Link for reference on return value in gfg](https://www.geeksforgeeks.org/python-return-statement/)

### example of return

```python
def greet(input):
    if "hello" in input:
        return "hello, there"
    else:
        return "I'm not sure what you mean"

greeting = greet("hello, computer")
print(greeting + " Carter")
```

The value of return value is that it allows us to modify things throughout our code and use the output of some function later on. A side effect is slightly different as it simply produces some change immediately.

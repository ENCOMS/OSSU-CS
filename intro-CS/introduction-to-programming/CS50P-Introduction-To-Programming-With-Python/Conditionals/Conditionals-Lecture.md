# Topic: Conditionals

# Link: [Learning.edx - CS50P](https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@d25e27c90c304b0293d1f8dbda47c1b6/block-v1:HarvardX+CS50P+Python+type@vertical+block@30350cbeec734204b98c3f2d7e798c40)

```sh
> bigger than
>= bigger or equal than
< lesser than
<= lesser or equal than
== equal
!= not equal
```

##Logic decisions
###If

```
x = int(input("What's x?))
y = int(input("What's y?))

if x < y:
    print("x is less than y")
```

- keyword if 
- boolean comparators
- : indicates that the following code will run if the boolean expression is true.

###Tip:
In difference to other language the boolean expression is not inside a () nor use {} to hold the decision code.

For this in python we have the ":"

##New code addition

```
if x < y:
    print("x is less than y")

if x > y:
    print("x is greater than y")

if x == y:
    print("x is equal to y")
```

##Using a flow-chart to illustrate the previous code:

- [flow-chart](./compare.dio) - flow chart of previous code.

- Oval shape: Start / End of the algorithm
- Diamond shape: Based on the answer go left or right, true or false
- Rectangular: indicates what to do if true.

##Improvements:
- Make these conditions potentially mutually exclusive.
- The use else if, in this case in python is elif
- Writing a better code lane the foundation of better developer in the future.

##elif code modification:

```
if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")

elif x == y:
    print("x is equal to y")
```

##Eliminating the need of the third question
```
if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")

else:
    print("x is equal to y")
```

##Or operator, if one or the other comparator is true run the code.
if x < y or x > y:
    print("x is not equal to y")

else:
    print("x is equal to y")

##Question to ask if we want to do a better code:
- Could my code be better?
- Could my code by simpler?
- Could I improve this code further?
- Could I improve the design?
- Could I ask fewer questions?
- Could I tighten it up?

##The use of not equal != or ==
With this we can simplify more our code.

if x != y:
    print("x is not equal to y")

else:
    print("x is equal to y")

or 

if x == y:
    print("x is equal to y")

else:
    print("x is not equal to y")

##And operator (Code example in grade.py file)

score = int(input("Score: "))

##First Approach:
This code do as intended, but we could asking the questions if we can do better, tight, efficient code, we can do some changes.

```
if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 89:
    print("Grade: B")
elif score >= 70 and score < 79:
    print("Grade: C")
elif score >= 60 and score < 69:
    print("Grade: D")
else:
    print("Grade: F")
```

##Second approach:
Tight and aesthetic more hand like approach. Python allows us to nest the conditional if evaluation the same variable against other values.

```  
if  90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 89:
    print("Grade: B")
elif 70 <= score < 79:
    print("Grade: C")
elif 60 <= score < 69:
    print("Grade: D")
else:
    print("Grade: F")
``` 

## Third approach:
Thinking how we can improve this, we can eliminated the two questions of lower and higher range and simplified to use only the lower range, as if greater than the lower range is in the range of the score and if greater than next lower score is another grade until all is evaluated. This way is more tight, small and hopefully endure the time.

```    
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

##Parity:
If even or odd, if a number is divided by two the reminder is 0 is even, otherwise is odd.

##Tip: 
Is a good way to start solving problems using functions, is that you declare functions that you want to return the values that you need, as to take those values and continue to write the rest of the code, even if you don't even have a clue of how to write those functions that return the values that you need.

data type bool: could only be True or False

# in parity.py:

## First approach:

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0
        return True #this is a bool expression
    else:
        return False #this is another bool expression

main()

If we as ourself can we improve on the design of this code?
Can I make this particular program better?


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

## another way to approach this case:

## match 
Is similar in spirit to switch in other languages. Is implemented in recent python.

we can create another example:
houses.py based in Harry potter houses.

# first approach
name = input("What's your name? ")

if name == "Harry":
    print("Gryffindor")
if name == "Hermione":
    print("Gryffindor")
if name == "Ron":
    print("Gryffindor")
if name == "Draco":
    print("Slytherin")
else:
    print("Who?")

# second approach

"""
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
if name == "Draco":
    print("Slytherin")
else:
    print("Who?")
"""
    
# third approach using match, but not optimize:

"""
match name:
    case "Harry":
            print("Gryffindor")
    case "Hermione":
            print("Gryffindor")
    case "Ron":
            print("Gryffindor")
    case "Draco":
            print("Slytherin")
    case _: # _ The underscore it's meant to say whatever case has not yet been handled
            print("Who?")
"""
            
# fourth case, match but more optimize:

match name:
    case "Harry" | "Hermione" | "Ron": # The | in this case of match is equivalent of an or
            print("Gryffindor")
    case "Draco":
            print("Slytherin")
    case _: # _ The underscore it's meant to say whatever case has not yet been handled
            print("Who?")





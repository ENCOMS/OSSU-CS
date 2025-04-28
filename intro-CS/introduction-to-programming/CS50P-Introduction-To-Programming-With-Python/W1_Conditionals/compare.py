x = int(input("What's x? "))
y = int(input("What's y? "))

"""
#step 1 of the code
if x < y:
    print("x is less than y")
#My personal addition to the code with an else
else:
    print("x is greater than y")

#note: the code is too simple atm
"""

"""
#step 2 of the code
if x < y:
    print("x is less than y")

if x > y:
    print("x is greater than y")

if x == y:
    print("x is equal to y")

#too many if, taking a toll in performance.
"""

"""
#step 3 of the code
if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")

elif x == y:
    print("x is equal to y")
"""

"""
#with the use use of else if (elif),the performance is improve since it take less decisions
    
#step 4 of the code
if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")

else:
    print("x is equal to y")
#with this else, the performance is increased even more since it ask fewer questions.
"""


"""
#with the use Or operator, we can say if one or the other decision is true run the code, else do something else.
    
#step 5 of the code
if x < y or x > y:
    print("x is not equal to y")

else:
    print("x is equal to y")
#with this Or, the performance is increased even more since it ask fewer questions.
"""

"""
#with the use != not equal operator, we can say right away if one or the other value is equal or not equal.

#step 6 of the code
if x != y:
    print("x is not equal to y")

else:
    print("x is equal to y")

#with this !=, the performance is increased even more since it ask fewer questions.

if x == y:
    print("x is equal to y")

else:
    print("x is not equal to y")
"""

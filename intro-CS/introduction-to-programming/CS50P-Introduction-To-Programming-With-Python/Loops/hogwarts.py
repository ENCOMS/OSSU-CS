#first interaction
# is pretty lame since we have to hardcode the iterations.

'''
students = ["Hermione", "Harry", "Ron"]
print(students[0])
print(students[1])
print(students[2])
'''

#Second iteration
# we can use a for loop, in this case using the control variable to hold one value of the list in each iteration, then print the value of that position.

'''
students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)
'''

#Tip: the name of the iteration variable cannot be in this case "_" since it would make the code too cryptic, as no one in the future would know you are referring to even you in the future.

#it would be good practice to place a name of the variable in plural, as to know it have many values in it. and the iteration value the same name but writing it in singular.

#In other languages, the variable for iteration need to be initialized, commonly 0. In python no.

#Third iteration

'''
#in this case we change the variable for the range function using the len function on the students list as to obtain the actual length of the list.

#the function len return the actual length of items a list hold. in this case 3
students = ["Hermione", "Harry", "Ron"]

#for iterate the list assigning the a value to i, for each item of the list.
for i in range(len(students)):
    print(i + 1, students[i])
'''

#Dictionaries:

#first iteration: very simple: not efficient since we are repeating ourself. bad habit.

'''
students = { 
    "Hermione": "Gryffindor", 
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor", 
    "Draco": "Slytherin",
}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])
'''

# second iteration: much better since we are using a for to iterate the list, but since we are using the default construct of the for, we don't have much control of what or where iterate.

'''
students = { 
    "Hermione": "Gryffindor", 
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor", 
    "Draco": "Slytherin",
}

for student in students:
    print(student)
'''

# like this we are only printing the keys, but not the content of each key.

# third iteration: in this we gonna access the dictionaries with each key to obtain the house of each student name (key).

'''
students = { 
    "Hermione": "Gryffindor", 
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor", 
    "Draco": "Slytherin",
}

for student in students:
    print(student, students[student], sep=", ")
'''

#this way we can access using the key the content of the dictionaries, much like the index on a list.
# since we need a separator, we can use the print parameter "sep" of separator so to print a ", " to separate the name and the house.

# fourth iteration: what if we work with more information about the students, we can create a list of dictionaries to help us keep the information organize, accessible and having the possibility of faster retrieval, this last is part of the major functions of python.

# first we create a list and inside the dictionaries

'''
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"}, 
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"}, 
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"}, 
    {"name": "Draco", "house": "Slytherin", "patronus": None} #None is a keyword to indicate no value here. 
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
'''

#we iterate each index of the list and dictionaries on that index, retrieve the information we want using the key values.

# we still use the sep parameter to separate the outputs.

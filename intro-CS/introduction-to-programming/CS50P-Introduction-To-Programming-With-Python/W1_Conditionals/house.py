
#creating the name variable
name = input("What's your name? ")

# first approach

"""
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
"""

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
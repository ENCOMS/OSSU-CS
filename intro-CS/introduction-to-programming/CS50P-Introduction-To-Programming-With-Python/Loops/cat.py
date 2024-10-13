#Little app for meow

'''
#First interaction, not optimize, we repeat ourself and poorly design:
print("meow")
print("meow")
print("meow")
'''

'''
#Second interaction, not optimize but works:
i = 3
while i != 0:
    print("meow")
    i = i - 1 #if we don't add a control for our loop, will continue forever. In this case it will decrease the valor of i
'''

'''
#Third interaction, not optimize, poorly design:
i = 0
while i < 3: #in this case we don't use the less or equal, since we don't want it to reach 3, only less than 3.
    print("meow")
    i += 1 #In this case instead of i = i + 1 we gonna use a special syntax, popular in code.

#Note: in other languages it can be ++ or -- but is different in python
'''

#for loop
'''
# first iteration, a poorly design for loop.

for i in [0,1,2]:
    print("meow")

#Since the list consist of 3 items, it prints 3 meows. But is poorly design as is a good habit to check for corner cases, to take to the extreme the code and see if functional and easy to use. Is poorly design as if the list is longer or too big, would be impractical to use.
'''

'''
# second iteration, some improvement to the design for loop.

for i in range(10): #instead of manually setting the list of values, we use a python function that will set our range of values to evaluate.
    print("meow")

#This improves over the last part. But we can improve a little more.
''' 

'''
# Third iteration, more improvement to the design for loop using a pythonic solution.

for _ in range(10): #We change the variable that iterate to a _ in this case since we don't use or won't use the result of the iteration.
    print("meow")
'''

'''
# Fourth iteration, is a pythonic way in python to do something like the for, but is not that readable.

print("meow\n" * 3, end="")

#- we can do some iteration even if is a string, using multipliers, so is kinda like the for
#- we use the new line \n in the string to force a new line at the end.
#- we change the default end for a "" so there wont be an empty space.
'''

'''
while True: #while this true always ask
    n = int(input("What's n? "))
    if n > 0: #if enter a value that is not, it will keep asking. If we enter an integer greater than 0, it will exit the loop.
        break #keyword for exit the loop

# Instead of asking if less than 0 and create more lines of code, we use a mutual opposition question, if greater than 0, break (stop the loop). This is common paradigm in python or any language.

for _ in range (n): #take our user input
    print("meow") #print as many n input
'''

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:#allways start the loop and 
        n = int(input("What's n? "))
        if n > 0: #continue if the condition is met
            break #or simple return, since doing a return will exit the function too
    return n #or we can simple declare

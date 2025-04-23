# Ask use for their name
#name = input("What's your name? ").strip().title()

#Say hello to the user

#this one is concatenation
#print("hello, " + name)

#with , it let us include multiple arguments, it automatically add an extra space
#print("hello,", name)

#split user's name into first and last name
#name = name.split(" ")

#print(f"hello, {name}")

#first, last = name.split(" ")
#print(f"hello, {first}")

#defining a function hello

#def hello(To="world"):
    #we added to the function to accept a parameter To
#    print("hello,", To)



#hello()
#name = input("What's your name? ")
#hello(name)


def main():
    name = input("What's your name? ")
    hello()
    hello(name)
    

def hello(To="world"):
    print("hello,", To)


main()






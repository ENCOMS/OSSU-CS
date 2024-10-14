#indoor voice app

#Requirements
#------------
#A program that prompts the use input and outputs that same input in lowercase.
#Punctuation and whitespace should be outputted unchanged.
#Optional: passing the user prompt as an argument to input.


def main():
    #We ask the user to input his name or anything he want to type and we use a method called lower() to change to lower case if there are any Capitalize word.
    userInput = input("please write your full name: ").lower()

    #Here we print the result in a format string
    print(f"Hi {userInput}")




main()
#faces app

#Requirements
#------------
#implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.

#Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input, and prints the result. 

#You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input. Be sure to call main at the bottom of your file.



#defining main function
def main():
    #We ask the user to input of his name or anything he wants.
    userInput = input("please write your full name or anything you like: ")

    #Here we print the result in a format string
    
    # We use the method convert() to change text emoticons to the respective emoji, returning a unchanged string if no emoticon present.
    userInputConverted = convert(userInput)
    
    print(userInputConverted)


#function called convert
def convert(string):
    #created a dictionary
    stringToConvert = {":)": "🙂", ":(": "🙁"}
    #A for loop as to check the string for the values to change.
    for emoji in stringToConvert.keys():
        string = string.replace(emoji, stringToConvert[emoji])
    #retun the converted string
    return string

#calling main
main()
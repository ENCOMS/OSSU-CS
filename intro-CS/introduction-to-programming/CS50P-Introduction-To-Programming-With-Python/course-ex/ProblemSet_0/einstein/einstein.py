#einstein app

#Requirements
#------------
# Implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.


#defining main function
def main():
    #We ask the user to input of his name or anything he wants.
       
    userInput = input("m = ")

    #Here assign the result to a variable so to make it more readeble
    userInputResults = formulaEinstein(userInput)
    
    #Here we print the result
    print(userInputResults)


#function called formulaEinstein
def formulaEinstein(number):
    
    result = int(number) * (300000000 * 300000000)
    
    return result

#calling main
main()
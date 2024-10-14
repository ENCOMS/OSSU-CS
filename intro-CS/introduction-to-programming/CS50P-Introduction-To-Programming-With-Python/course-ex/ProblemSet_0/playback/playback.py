#playback app

#Requirements
#------------
#Implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods)


def main():
    #We ask the user to input his name or anything he want to type and we use a method called replace() to change ' ' to ...
    userInput = input("please write your full name or anything you fancy: ").replace(' ','...')

    #Here we print the result in a format string
    print(f"{userInput}")




main()
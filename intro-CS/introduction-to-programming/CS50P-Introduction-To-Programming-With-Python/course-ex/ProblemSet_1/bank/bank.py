# In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.


def main():
    greeting = input("Greeting: ").lower().strip()
    greetingCheck(greeting)


def greetingCheck(greet):
    if greet[:5] == "hello":
        return print("$0")
    elif greet[:1] == "h":
        return print("$20")
    else:
        return print("$100")
        
main()


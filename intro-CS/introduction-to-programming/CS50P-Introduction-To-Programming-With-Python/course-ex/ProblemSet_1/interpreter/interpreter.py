"""
CS50P exercise:
In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer

"""


#First approach:

def main():
    toInterpret = input("Expression: ").lower().strip()
    print(theInterpreter(toInterpret))


def theInterpreter(i):
    x, y, z = i.split(" ")

    x = float(x)
    z = float(z)

    match y:
        case "+":
            return round(x + z, 1)
        case "-":
            return round(x - z, 1)
        case "*":
            return round(x * z, 1)
        case "/":
            if z == 0:
                return "It cannot be divided by 0"
            else:
                return round(x / z, 1)
        case _:
            print("Not a valid expression")


main()


"""
#Second approach

def main():
    toInterpret = input("Expression: ").lower().strip()
    print(theInterpreter(toInterpret))


def theInterpreter(i):
    try:
        result = eval(i)
    except ZeroDivisionError:
        return 'Error: Division by zero is not allowed.'
    return round(float(result), 1)


main()
"""
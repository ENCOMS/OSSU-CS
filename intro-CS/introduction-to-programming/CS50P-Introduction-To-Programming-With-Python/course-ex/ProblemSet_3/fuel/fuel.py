'''
Fuel Gauge

Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.

Indicators:
- x and y must be integers
- prompt the use for x/y
- obtain x and y
- x have to be equal or greater than 1
- y have to equal or greater than x
- divide the two numbers
- transform to a rounded %
- if 1 or less E
- if 99 or more F
- 1/4 25%
- 2/4 50%
- 3/4 75%
- 4/4 F
- catch error ValueError or ZeroDivisionError and re-prompt the user (they must not know that there was an error)

'''


def fuel_check(prompt):
    try:
        a, b = input(prompt).split("/")
        result = round((int(a)/int(b))*100)
        
        if result > 100:
            fuel_check(prompt)
        elif result <= 1:
            print("E")
        elif result >= 99 and result <= 100:
            print("F")
        else:
            print(f"{result}%")

    except (ValueError, ZeroDivisionError):
        fuel_check(prompt)


def main():
    fuel_check("Fraction: ")


main()
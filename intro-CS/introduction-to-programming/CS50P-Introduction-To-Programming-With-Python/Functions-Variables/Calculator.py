
#user input is always text
#x = input("what is the value of x? ")
#y = input("what is the value of y? ")



#z = x + y

#output is the concatenated of xy
#to resolve the issue we can use the int() method to transform string to integers

#z = int(x) + int(y)

#print(z)

#nested functions
#x = int(input("what is the value of x? "))
#y = int(input("what is the value of y? "))

#print(x + y)

#z = round(x + y, 3)

#print(f"{z:,}")

#f approach

#z = x + y

#print(f"{z:.2f}")

# .2f indicates that the function return a float with two decimals

'''
def main():
    x = int(input("What's x? "))
    print("the square of x is= ", square(x))

def square(number):
    return number ** 2
    # ** is an exponential or we can use pow() method from python

'''
'''
def main():
    # Function calls with different numbers of arguments
    find_sum(1, 2, 3)
    find_sum(4, 9)

# Function with arbitrary number of arguments
def find_sum(*numbers):
    result = 0
    for num in numbers:
        result += num
    print("Sum =", result)
'''

def main():
    # Function calls with varying number of arguments
    add_numbers(2, 3) # Both arguments provided
    add_numbers(a=2) # Only 'a' provided, 'b' uses default value
    add_numbers() # No arguments provided, both defaults are used

# Function with default arguments
def add_numbers(a=7, b=8):
    sum = a + b
    print('Sum:', sum)


main()



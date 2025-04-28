# Sixth example: command-line arguments using sys module and argv or argument vector, vector stand for list
'''
import sys

print("hello, my name is", sys.argv[1])
'''

# Seventh example: handling human error
'''
import sys

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
'''

# Eighth example: checking for errors with if statements.
'''
import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])
'''

# Ninth example: separating the code we really want from the validators, using sys.exit to exit the program if not correct.
'''
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")


print("hello, my name is", sys.argv[1])
'''

# Tenth example: slices of a list using [start : end]
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)
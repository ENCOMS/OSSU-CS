#-- Flipping coin app--

#First example, import module
'''
import random

coin = random.choice(["heads", "tails"])
print(coin)
'''

#Second example, using from 'module' import 'function'
'''
from random import choice

coin = choice(["heads", "tails"])
print(coin)
'''

#-- Random number from a range of integers --

#Third example, using randint(a, b) function to randomize a range of numbers.
'''
import random

number = random.randint(1, 10) #10% change of any number from 1 to 10
print(number)
'''

#Fourth example, using random.shuffle(x) function to shuffle lists of items, passing the list but randomize.
'''
import random

cards = ["jack", "queen", "king"]

random.shuffle(cards)

#as to output the list not using the format that python use, we print only the cards using a for loop.

for card in cards:
    print(card)
'''
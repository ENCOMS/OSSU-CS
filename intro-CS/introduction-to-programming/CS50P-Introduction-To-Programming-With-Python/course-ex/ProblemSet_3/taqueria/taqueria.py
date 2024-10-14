'''
Taqueria

One of the most popular places to eat in Harvard Square is Felipe’s Taqueria, which offers a menu of entrees, per the dict below, wherein the value of each key is a price in dollars:


{
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


In a file called taqueria.py, implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. Treat the user’s input case insensitively. Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased.


indicators:
output:
Item: {user_input}
Total: $xx.xx

prompt user until control-d:
try:
    item = input()
except EOFError:
    ...


- ignore any input that ins't an item (reprompt)

- use titlecase as to transform the input to the same as the key in the chart

'''

def taqueria_food(prompt):
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    
    total = 0

    while True:
        try:
            item = input(prompt).title().strip()  
            if item in menu:
                total = total + menu.get(item)
                print(f"Total: ${total:.2f}")
            else: 
                continue
                
        except (EOFError, KeyboardInterrupt):
            return
    

def main():
    order = "Item: "
    taqueria_food(order)
   

main()




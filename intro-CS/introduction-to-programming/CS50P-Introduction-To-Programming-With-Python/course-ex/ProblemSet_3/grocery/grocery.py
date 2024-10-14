'''
In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.

indicadores:
- prompt the user for items (apple, banana, pera)
- one per line until ctrl+d
- output the user's grocery list in all uppercase
- sorted alphabetically by item
- prefixing each line with the number of times the user inputted that item.
- No need to pluralize the items.
- Treat the user's input case-insensitively.

'''


def grocery_list():
    list = {}
    try:
        while True:
            list = dict(sorted(list.items()))
            key = input().upper().strip()
            if key in list:
                list[key] = list[key]+1
            else:
                list.update({key: 1})
    except (EOFError, KeyboardInterrupt):
        print()
        for item in list:
            print(f"{list.get(item)} {item}")


def main():
    grocery_list()
   

main()
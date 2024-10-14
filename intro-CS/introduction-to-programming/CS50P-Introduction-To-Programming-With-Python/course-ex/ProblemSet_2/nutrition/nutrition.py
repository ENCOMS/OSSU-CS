'''
The U.S. Food & Drug Administration (FDA) offers downloadable/printable posters that “show nutrition information for the 20 most frequently consumed raw fruits …
in the United States. Retail stores are welcome to download the posters, print, display and/or distribute them to consumers in close proximity to the relevant foods in the stores.”

In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit,
per the FDA’s poster for fruits, which is also available as text. Capitalization aside, assume that users will input fruits exactly as written in the poster
(e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.

'''


def food_calories(food):
    # Made a dict inside a dict, as to access or add more data later
    nutrition_facts_dict = {
        'apple': {'calories': '130'},
        'avocado': {'calories': '50'},
        'banana': {'calories': '110'},
        'cantaloupe': {'calories': '50'},
        'grapefruit': {'calories': '60'},
        'grapes': {'calories': '90'},
        'honeydew melon': {'calories': '50'},
        'kiwifruit': {'calories': '90'},
        'lemon': {'calories': '15'},
        'lime': {'calories': '20'},
        'nectarine': {'calories': '60'},
        'orange': {'calories': '80'},
        'peach': {'calories': '60'},
        'pear': {'calories': '100'},
        'pineapple': {'calories': '50'},
        'plums': {'calories': '70'},
        'strawberries': {'calories': '50'},
        'sweet cherries': {'calories': '100'},
        'tangerine': {'calories': '50'},
        'watermelon': {'calories': '80'}
    }
    if food in nutrition_facts_dict:
        return print("Calories:", nutrition_facts_dict[food]['calories'])
    else:
        return print("")


def main():
    user_food = input("Item: ").lower().strip()
    food_calories(user_food)


main()
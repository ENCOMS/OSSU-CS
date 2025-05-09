"""
In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and 
 names with 
 commas and one and, as in the below:

Expected: 
Name: Liest
...
 
Output: 
Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl

"""

import inflect


def main():
    p = inflect.engine()

    list = []

    while True:
        try:
            user_input = input("Name: ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if "" != user_input != " ":
            list.append(user_input)
        else:
            break

    result = p.join(list)
    print(f"Adieu, adieu, to {result}")


if __name__ == "__main__":
    main()

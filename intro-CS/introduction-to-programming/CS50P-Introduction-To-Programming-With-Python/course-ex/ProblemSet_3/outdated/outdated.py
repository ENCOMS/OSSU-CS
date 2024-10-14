'''
In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:

[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.

Indicators:

- It can take date formatted as: 9/8/1636 like month/day/year
- It can take a date formatted as: September 8, 16363, Month day, year
- Should out put Year-Month-Day
- Should use the list provided.
- A month can take up to 31 days.
- No need to validate if a month has 28, 29, 30, or 31 days.
- If not the correct format, reprompt
- ctrl-d exit.

- check if first char is str or digit
- check if digit in first variable and second variable have is 1 or 2 digit len
- transform to int second and third variable.
- catch any error that is user input fault.


'''

'''

def date_converter(prompt):
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

    user_input = input(prompt).strip()

    if "/" in user_input:
        month, day, year = user_input.split("/")
        yy = int(year)
        mm = int(month)
        dd = int(day)
        
    elif "," in user_input:
        mod_user_input = user_input.replace(",","")
        month, day, year = mod_user_input.split(" ")
        yy = int(year)
        mm = int(months.index(month))+1
        dd = int(day)
    elif mm and dd >= 1 and mm <= 12 and dd <= 31:
        print(f"{yy:04}-{mm:02}-{dd:02}")
    else:
        date_converter(prompt)
'''

def is_day(dd):
    if len(dd) <= 2 and dd.isdigit() and int(dd) > 0 and int(dd) <= 31:
        return int(dd)
    else:
        raise ValueError("Not a valid day number")


def is_month(mm):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    if mm.isdigit() and int(mm) > 0 and int(mm) <= 12:
        return int(mm)
    elif mm.isalpha() and mm in months:
        return months.index(mm)+1
    else:
        raise ValueError("Not valid name or numeric Month")


def date_converter(prompt):
    user_input = input(prompt).strip()

    try:
        if user_input.find("/") and user_input[0].isdigit():
            month, day, year = user_input.split("/")
            yy = int(year)
            mm = is_month(month)
            dd = is_day(day)
        elif "," in user_input:
            mod_user_input = user_input.replace(",", "")
            month, day, year = mod_user_input.split(" ")
            yy = int(year)
            mm = is_month(month)
            dd = is_day(day)
        else:
            raise ValueError("Not a valid date format")
    except ValueError as e:
        print(f'ValueError: {e}')
        date_converter(prompt)

    print(f"{yy:04}-{mm:02}-{dd:02}")


def main():
    question = "Date: "
    date_converter(question)


main()
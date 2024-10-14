"""
Meal time app
Create the meal.py file

Suppose that you’re in a country where it’s customary to eat:
- breakfast between 7:00 and 8:00
- lunch between 12:00 and 13:00
- dinner between 18:00 and 19:00.

Implement a program that prompts the user for a time:
    "What time is it? "
and outputs whether:
    it’s breakfast time, lunch time, or dinner time.
If it’s not time for a meal:
    don’t output anything at all.

Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive.
For instance:
    whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.
    whether it’s 12:00, 12:01, 12:59, or 13:00, or anytime in between, it’s time for lunch.
    whether it’s 18:00, 18:01, 18:59, or 19:00, or anytime in between, it’s time for dinner.

Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format,
 to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).

an hour is 60 min

"""
"""
Meal time app

Process:
Create the meal.py file

Suppose that you’re in a country where it’s customary to eat:
- breakfast between 7:00 and 8:00
- lunch between 12:00 and 13:00
- dinner between 18:00 and 19:00.

Implement a program that prompts the user for a time:
    "What time is it? "
and outputs whether:
    it’s breakfast time, lunch time, or dinner time.
If it’s not time for a meal:
    don’t output anything at all.

Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive.
For instance:
    whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.
    whether it’s 12:00, 12:01, 12:59, or 13:00, or anytime in between, it’s time for lunch.
    whether it’s 18:00, 18:01, 18:59, or 19:00, or anytime in between, it’s time for dinner.

Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format,
 to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).

an hour is 60 min

"""
import re


def main():
    wTime = input("What time is it? ").lower().strip()
    printer(convert(wTime))


def convert(time):
    try:
        if ":" in time and time.endswith("am"):
            stud = re.sub("am",  "",  time).strip()
            hour, minutes = stud.split(":")

            hour = int(hour)
            minutes = int(minutes)

            result = hour+round(minutes/60, 2)
            return result

        elif ":" in time and time.endswith("pm"):
            stud = re.sub("pm",  "",  time).strip()
            hour, minutes = stud.split(":")

            hour = int(hour)
            minutes = int(minutes)

            result = (hour+12)+round(minutes/60, 2)
            return result

        else:
            hour, minutes = time.split(":")
            hour = int(hour)
            minutes = int(minutes)

            result = hour+round(minutes/60, 2)
            return result
    except:
        print("Wrong format or values!")


def printer(convertedTime):
    if 7.00 <= convertedTime <= 8.00:
        print("breakfast time")
    elif 12.00 <= convertedTime <= 13.00:
        print("lunch time")
    elif 18.00 <= convertedTime <= 19.00:
        print("dinner time")
    else:
        return


if __name__ == "__main__":
    main()
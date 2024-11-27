"""
Seasons of love problem

In a file called seasons.py, implement a program that prompts the user 
for their date of birth in YYYY-MM-DD format and then prints how old 
they are in minutes, rounded to the nearest integer, using English 
words instead of numerals, just like the song from Rent, without any 
and between words.

+ Since a user might not know the time at which they were born, assume, 
for simplicity, that the user was born at midnight (i.e., 00:00:00) on 
that date.

+ And assume that the current time is also midnight. In other words, 
even if the user runs the program at noon, assume that it’s actually
midnight, on the same date.

+ Use datetime.date.today to get today’s date, per
docs.python.org/3/library/datetime.html#datetime.date.today.

Requirements:
+ Ask input if user for input: "Date of Bird: "
+ Expect input only in integer in this format: "YYYY-MM-DD"
+ Expected output/input in terminal: Date of Bird: YYYY-MM-DD
+ In case of bad input: sys.exit("Invalid inputs")
+ Prints how old they are in minutes, rounded to the nearest integer,
using English words instead of numerals (inflect library)
+ Asume user was born at midnight 00:00:00 on that date
+ Asume that the current time is also midnight. In other words, even
if the user runs the program at noon, asume that it's actually midnight,
on the same date.
+ Use datetime.date.today to get today's date.


Example Assuming recorded January 1, 2000:
Valid inputs
Date of Bird: 1999-01-01
Output
Five hundred twenty-five thousand, six hundred minutes
525600

Valid inputs
Date of Birth: 1999-12-31
Output
One thousand, four hundred forty minutes
1440

Invalid inputs
Date of Bird: January 1, 1999
Output
Invalid date

"""

from datetime import date
import sys
import inflect
import re


class Time_born:
    def __init__(self, minutes):
        self.minutes = minutes

    @staticmethod
    def get_date():
        if len(sys.argv) > 1 and ".py" in sys.argv[0]:
            user_date_birth = sys.argv[1]
        else:
            user_date_birth = input("Date of Birth: ")
        try:
            return date.fromisoformat(user_date_birth)
        except ValueError:
            sys.exit("Invalid inputs")

    @classmethod
    def min_since(cls, date_birth, fixed_date=None):
        if fixed_date != None:
            try:
                today = date.fromisoformat(fixed_date)
            except ValueError:
                sys.exit("Invalid fixed date")
        else:
            today = date.today()
        if date_birth > today:
            sys.exit("Invalid date")
        date_birth = today - date_birth
        minutes = int(date_birth.total_seconds() / 60)
        return cls(minutes)

    def sing(self):
        words = inflect.engine().number_to_words(self.minutes)
        corrected_w = re.sub(r" and+", "", words).capitalize()
        return f"{corrected_w} minutes"

    def __str__(self):
        return f"{self.minutes} minutes"


def main():
    born_date = Time_born.get_date()
    minutes = Time_born.min_since(born_date)
    print(minutes.sing())


if __name__ == "__main__":
    main()

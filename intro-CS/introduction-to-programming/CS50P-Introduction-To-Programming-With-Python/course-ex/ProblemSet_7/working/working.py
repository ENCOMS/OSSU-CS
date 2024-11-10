import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    convertion_dic = [
        {
            "12": "00",
            "1": "01",
            "2": "02",
            "3": "03",
            "4": "04",
            "5": "05",
            "6": "06",
            "7": "07",
            "8": "08",
            "9": "09",
            "10": "10",
            "11": "11",
        },
        {
            "12": "12",
            "1": "13",
            "2": "14",
            "3": "15",
            "4": "16",
            "5": "17",
            "6": "18",
            "7": "19",
            "8": "20",
            "9": "21",
            "10": "22",
            "11": "23",
        },
    ]

    pattern = (
        r"^(?P<from_12_hour>1[0-2]|[0-9])(?:(?P<from_12_min>:[0-5][0-9]))? (?P<from_12_meridian>PM|AM)? to "
        r"(?P<to_12_hour>1[0-2]|[0-9])(?P<to_12_min>:[0-5][0-9])? (?P<to_12_meridian>PM|AM)?$"
    )

    if matches := re.search(pattern, s):
        if matches.group("from_12_meridian") and matches.group("to_12_meridian"):
            from_hour, to_hour, from_min, to_min, from_mer, to_mer = (
                matches.group("from_12_hour"),
                matches.group("to_12_hour"),
                matches.group("from_12_min"),
                matches.group("to_12_min"),
                matches.group("from_12_meridian"),
                matches.group("to_12_meridian"),
            )

            if from_mer == "AM":
                from_hour = f"{convertion_dic[0][from_hour]}"
            if from_mer == "PM":
                from_hour = f"{convertion_dic[1][from_hour]}"
            if to_mer == "AM":
                to_hour = f"{convertion_dic[0][to_hour]}"
            if to_mer == "PM":
                to_hour = f"{convertion_dic[1][to_hour]}"
            if from_min == None:
                from_min = ":00"
            if to_min == None:
                to_min = ":00"
            return f"{from_hour}{from_min} to {to_hour}{to_min}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()

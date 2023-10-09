'''
Tristan Deveyra
2057603
'''

import datetime


def is_valid_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%B %d, %Y")
        return True
    except ValueError:
        return False


def format_date(date_str):
    date = datetime.datetime.strptime(date_str, "%B %d, %Y")
    return date.strftime("%m/%d/%Y")


dates = []
while True:
    date_str = input()
    if date_str == "-1":
        break
    if is_valid_date(date_str):
        dates.append(format_date(date_str))

current_date = datetime.datetime.now()

valid_dates = [date for date in dates if datetime.datetime.strptime(date, "%m/%d/%Y") <= current_date]

for date in valid_dates:
    print(date)

with open("parsedDates.txt", "w") as output_file:
    for date in valid_dates:
        output_file.write(date + "\n")

# ---------------------------------------------------------------------------- #
#                                  Date & Time                                 #
# ---------------------------------------------------------------------------- #
# Ref: https://www.w3schools.com/python/python_datetime.asp
# Ref: https://docs.python.org/3/library/datetime.html
import datetime

# ---------------------------- Current date & time --------------------------- #
dateTimeNow = datetime.datetime.now()
print("Current date & time: ", dateTimeNow)
print("Year: ", dateTimeNow.year)
print("Day: ", dateTimeNow.strftime("%A"))

# --------------------------- creating date & time --------------------------- #
myDateTime = datetime.datetime(2021, 9, 13)
print("myDateTime", myDateTime)

#? python3 -m calendar 2000

'''
import calendar
from datetime import datetime

def highlight_today(year):
    today = datetime.today()
    current_year = today.year
    current_month = today.month
    current_day = today.day

    for month in range(1, 13):
        cal = calendar.monthcalendar(year, month)
        print(calendar.month_name[month])
        print("Mo Tu We Th Fr Sa Su")
        for week in cal:
            week_str = ""
            for day in week:
                if day == 0:
                    week_str += "   "
                elif year == current_year and month == current_month and day == current_day:
                    week_str += f"[{day:2d}] "
                else:
                    week_str += f"{day:2d} "
            print(week_str)
        print("\n")

# Highlight the current date for the year 2024
highlight_today(2024)
'''
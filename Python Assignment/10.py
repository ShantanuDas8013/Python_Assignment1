def is_leap_year(year):
    """Return True if the given year is a leap year, else False."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(month, year=None):
    """Return the number of days in the given month."""
    month_days = {
        "January": 31,
        "February": 29 if year and is_leap_year(year) else 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }
    return month_days.get(month, "Invalid month")

month = input("Enter the month name: ")

if month == "February":
    year = int(input("Enter the year: "))
    days = days_in_month(month, year)
else:
    days = days_in_month(month)

if days == "Invalid month":
    print("Invalid month entered.")
else:
    print(f"The number of days in {month} is: {days}")

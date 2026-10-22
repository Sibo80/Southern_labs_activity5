#Author: Sibonile

def is_leap_year(year):
    """
    This determines whether a given year is a leap year.

    param:The year to check
    return: True if the year is a leap year,otherwise False.
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def get_day_of_the_week(month, day, year):
    """
    This determines the day of the week for given date
    
    param:
          month:the month of the date
          day:the day of the date
          year:the year of the date
    """
    year_number = year % 100
    twelves = year_number // 12
    remainder = year_number % 12
    fours = remainder // 4

    if month == 1:
        month_code = 1
    elif month == 2:
        month_code = 4
    elif month == 3:
        month_code = 4
    elif month == 4:
        month_code = 0
    elif month == 5:
        month_code = 2
    elif month == 6:
        month_code = 5
    elif month == 7:
        month_code = 0
    elif month == 8:
        month_code = 3
    elif month == 9:
        month_code = 6
    elif month == 10:
        month_code = 1
    elif month == 11:
        month_code = 4
    else:
        month_code = 6

    total = twelves + remainder + fours + day + month_code

    if year >= 1600 and year <= 1699:
        total = total + 6
    elif year >= 1700 and year <= 1799:
        total = total + 4
    elif year >= 1800 and year <= 1899:
        total = total + 2
    elif year >= 2000 and year <= 2099:
        total = total + 6
    elif year >= 2100 and year <= 2199:
        total = total + 4

    if (month == 1 or month == 2) and is_leap_year(year):
        total = total + 6

    day_number = total % 7

    if day_number == 0:
        return "Saturday"
    elif day_number == 1:
        return "Sunday"
    elif day_number == 2:
        return "Monday"
    elif day_number == 3:
        return "Tuesday"
    elif day_number == 4:
        return "Wednesday"
    elif day_number == 5:
        return "Thursday"
    else:
        return "Friday"

def main():
    print("Sunday" == get_day_of_the_week(12, 25, 2022))
    print("Friday" == get_day_of_the_week(8, 26, 2022))
    print("Thursday" == get_day_of_the_week(10, 5, 1972))
    print("Wednesday" == get_day_of_the_week(2, 3, 2016))
    print("Monday" == get_day_of_the_week(12, 18, 1899))

main()

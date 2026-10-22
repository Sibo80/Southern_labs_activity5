#Author: Sibonile

def is_leap_year(year):
<<<<<<< HEAD
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
=======
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


user_year = int(input("Enter a year: "))

if is_leap_year(user_year):
    print(f"{user_year} is a leap year.")
else:
    print(f"{user_year} is not a leap year.")


def get_day_of_the_week(month, day, year):
    month_codes = [0, 1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]

    last_two = year % 100
    first = last_two // 12
    second = last_two % 12
    third = second // 4

    total = first + second + third + day + month_codes[month]

    # Leap year adjustment
    if is_leap_year(year) and (month == 1 or month == 2):
        total -= 1
>>>>>>> cbf9174667cdbcab323508e72cef0060ea84645c

    # Century codes
    if 1600 <= year <= 1699:
        total += 6
    elif 1700 <= year <= 1799:
        total += 4
    elif 1800 <= year <= 1899:
        total += 2
    elif 2000 <= year <= 2099:
        total += 6
    elif 2100 <= year <= 2199:
        total += 4

    if (month == 1 or month == 2) and is_leap_year(year):
        total = total + 6

<<<<<<< HEAD
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
=======
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return days[result]
>>>>>>> cbf9174667cdbcab323508e72cef0060ea84645c

def main():
    print("Sunday" == get_day_of_the_week(12, 25, 2022))
    print("Friday" == get_day_of_the_week(8, 26, 2022))
    print("Thursday" == get_day_of_the_week(10, 5, 1972))
    print("Wednesday" == get_day_of_the_week(2, 3, 2016))
    print("Monday" == get_day_of_the_week(12, 18, 1899))

main()


# Author: Sibonile

def is_leap_year(year):
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

    result = total % 7

    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return days[result]


def main():
    print("Sunday" == get_day_of_the_week(12, 25, 2022))
    print("Friday" == get_day_of_the_week(8, 26, 2022))
    print("Thursday" == get_day_of_the_week(10, 5, 1972))
    print("Wednesday" == get_day_of_the_week(2, 3, 2016))
    print("Monday" == get_day_of_the_week(12, 18, 1899))


main()


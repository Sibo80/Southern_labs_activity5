# Author: Sibonile

  def is_leap_year(year):

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
               print("True")
            else:
                print("False")
        else:
            print("True")
    else:
        print("False")

user_year = int(input("enter a year: "))

 if is_leap_year(user_year):
 else:
     print(f"{user_year} is not leap year.")


def get_day_of_the_week(month, day, year)0:
    month_codes = [0, 1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]

    last_two = year % 100
    first = last_two // 12
    second = last_two % 12
    third = second // 4

    total = first + second + third + day + month_codes[month]

    if is_leap_year(year) and (month == 1 or month == 2):
        total = total + 6

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

    result = total % 7

    if result == 0:
        return "Saturday"
    elif result == 1:
        return "Sunday"
    elif result == 2:
        return "Monday"
    elif result == 3:
        return "Tuesday"
    elif result == 4:
        return "Wednesday"
    elif result == 5:
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

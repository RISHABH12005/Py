'''  Write a Python program to generate the next 15 leap years starting from a given year.
Populate the leap years into a list and display the list. '''
def leap_years(start):
    leap_years = []
    year = start
    while len(leap_years) < 15:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap_years.append(year)
        year += 1
    return leap_years
start = int(input("Enter the starting year: "))
print(leap_years(start))

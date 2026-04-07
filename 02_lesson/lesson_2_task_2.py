def is_year_leap(year):
    return year % 4 == 0


i = 2020
result = is_year_leap(i)
print("год", i, ":", result)

def is_year_leap(year):
    if ( year % 4 == 0):
     return True
    else:
     return False
    

leap_year = 2024
not_leap_year = 2023

leap_year_result = is_year_leap(leap_year)
not_leap_year_result = is_year_leap(not_leap_year)

print(f"Year is {leap_year} : {leap_year_result} ")  
print(f"Year is {not_leap_year} : {not_leap_year_result}")  
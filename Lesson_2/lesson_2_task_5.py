def month_to_season(n):
    if n in [9, 10, 11]:
        return "Autumn"
    elif n in [12, 1, 2]:
        return "Winter"
    elif n in [3,4,5]:
        return "Spring"
    elif n in [6,7,8]:
        return "Summer"
    else:
        return "No season found"

for loop in range (1, 14):
 terminal = int(input("Select number to get a season : "))
 season = month_to_season(terminal)
 print(f"{terminal} : {season}")
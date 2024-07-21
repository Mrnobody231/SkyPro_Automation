def bank (money, year):
    interest_rate = 0.10

    for amount_per_year in range(year):
        amount_per_year = money + (money * interest_rate)
    return amount_per_year 

total_amount = bank(1000, 2025)
print(total_amount)
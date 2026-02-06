import calendar

year = int(input("Enter the year you want: ")) # User inputs year
month = int(input("Enter the month you want: ")) # User inputs month

while month < 1 or month > 12: # Validating user's input
    month = int(input("Invalid! Enter the month you want(1 to 12): ")) # User re-inputs month

print("")
print(calendar.month(year, month)) # Outputting month
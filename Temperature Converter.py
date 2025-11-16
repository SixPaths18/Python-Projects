conversions = ["1. Celsius → Fahrenheit", "2. Fahrenheit → Celsius", "3. Celsius → Kelvin", "4. Kelvin → Celsius", "5. Fahrenheit → Kelvin", "6. Kelvin → Fahrenheit"]

for conversion in conversions:
    print(conversion)

# Inputting choice and error handling
choice = int(input("Choose a conversion(1 to 6): "))
if choice < 1 or choice > 6:
    print("Invalid choice!")
    exit()

# Inputing temperature and error handling
temperature = input("Enter the temperature: ")
try:
    tempDigit = float(temperature)
except ValueError:
    print("Invalid temperature!")
    exit()

# Outputting conversion
if choice == 1: print(f"{temperature}°C = {tempDigit * 9/5 + 32}°F")
if choice == 2: print(f"{temperature}°F = {(tempDigit - 32) * 5/9}°C")
if choice == 3: print(f"{temperature}°C = {tempDigit + 273.15}K")
if choice == 4: print(f"{temperature}K = {tempDigit - 273.15}°C")
if choice == 5: print(f"{temperature}°F = {(tempDigit - 32) * 5/9 + 273.15}K")
if choice == 6: print(f"{temperature}K = {(tempDigit - 273.15) * 9/5 + 32}°F")
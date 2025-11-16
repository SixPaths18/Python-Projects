password = input("Enter you password: ") # User inputs password

points = 0 # Initial number of points

# Password containing each of these elements
upper = False
lower = False
digit = False
special = False
diversity = 0

# Adding points based on length
if 8 <= len(password) <= 11: points += 1
if 12 <= len(password) <= 15: points += 2
if len(password) >= 16: points += 3

# Judging whether password contains each element
for char in password:
    if char.isupper():
        upper = True
    elif char.islower():
        lower = True
    elif char.isdigit():
        digit = True
    else:
        special = True

# Adding points based on containing elements
if upper: points += 1; diversity += 1
if lower: points += 1; diversity += 1
if digit: points += 1; diversity += 1
if special: points += 1; diversity += 1

# Adding points based on diversity
if diversity == 3: points +=1
if diversity == 4: points += 2

# Finding any repeated values
for i in range(0, len(password) - 2):
    if password[i] == password[i+1] == password[i+2]:
        points -= 1
        break

# Finding patterns
for i in range(0, len(password) - 2):
    if ord(password[i]) == ord(password[i+1]) + 1 == ord(password[i+2]) + 2:
        points -= 1
        break
    if ord(password[i]) == ord(password[i+1]) - 1 == ord(password[i+2]) - 2:
        points -= 1
        break

# Finding common keyboard patterns
keyboard_patterns = ["qwerty", "asdf", "zxcv", "1234", "9876"]
for pattern in keyboard_patterns:
    if pattern in password.lower():
        points -= 2

# Finding common weak passwords
weak_words = ["password", "admin", "letmein", "123456", "qwerty"]
for word in weak_words:
    if word in password.lower():
        points -= 2

# Outputting strength of password based on points
if points <= 2: print("❌ Password is very weak")
if points == 3 or points == 4: print("⚠️ Password is weak")
if points == 5 or points == 6: print("🙂 Password is medium")
if points == 7 or points == 8: print("💪 Password is strong")
if points >= 9: print("🔥 Password is very strong")
import random

# Storing different characters for password
uppercase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowercase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","]","{","}",";",":",",",".","<",">","?","/","|","`","~"]

options = [uppercase, lowercase, numbers, symbols]

length = random.randint(12, 16) # Generating random length of a password

passwordArray = []

# Ensuring that password contains at least one type of character set
passwordArray.append(random.choice(uppercase))  
passwordArray.append(random.choice(lowercase)) 
passwordArray.append(random.choice(numbers))  
passwordArray.append(random.choice(symbols)) 

for i in range(length-4): 
    # Generating random character
    character = random.choice(options)
    char = random.choice(character)

    # Adding character to string
    passwordArray.append(char)

random.shuffle(passwordArray) # Randomising password so not predictable

password = ""

# Making password string
for i in range(length):
    password += passwordArray[i]

print(f"Your password is: {password}")
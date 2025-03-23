import random # Importing random module

botPoints = 0 # Initial points for bot
userPoints = 0 # Initial points for user

for i in range(0, 11): # Running 11 times
    botChoice = random.choice(["rock", "paper", "scissors"]) # Bot chooses
    userChoice = input("Enter rock, paper or scissors: ") # User chooses
    
    # User input not valid
    while userChoice.lower() not in ["rock", "paper", "scissors"]:
        userChoice = input("Invalid! Enter rock, paper or scissors: ")

    # Bot chooses rock
    if botChoice == "rock" and userChoice == "rock":
       print("Tie!")
    elif botChoice == "rock" and userChoice == "paper":
       print("You win!")
       userPoints += 1
    elif botChoice == "rock" and userChoice == "scissors":
       print("Bot wins!")
       botPoints += 1

    # Bot chooses paper
    elif botChoice == "paper" and userChoice == "rock":
       print("Bot wins!")
       botPoints += 1
    elif botChoice == "paper" and userChoice == "paper":
       print("Tie!")
    elif botChoice == "paper" and userChoice == "scissors":
       print("You win!")
       userPoints += 1

    # Bot chooses scissors
    elif botChoice == "scissors" and userChoice == "rock":
       print("You win!")
       userPoints += 1
    elif botChoice == "scissors" and userChoice == "paper":
       print("Bot wins!")
       botPoints += 1
    elif botChoice == "scissors" and userChoice == "scissors":
       print("Tie!")

print("Your points:", userPoints) # Final user points
print("Bot points:", botPoints) # Final bot points

if botPoints > userPoints: # Bot wins
   print("Bot wins the tournament!")
elif botPoints < userPoints: # User wins
   print("You win the tournament!")
else: # Tie
   print("Tournament is a tie!")
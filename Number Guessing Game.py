import random   # Importing random module

number = random.randint(0, 100)   # Random number
tries = 0   # Initial tries

# Main loop
while True:
    guess = int(input("Enter a number between 0 and 100: "))   # Player's guess
    tries += 1   # Increment of tries

    # Guess is correct 
    if guess == number:
        print("Well done! You guessed correctly and it took you", tries, "tries.")
        break   # Game over when guess is correct
    # Guess is lower than number
    elif guess < number:
        print("Too low!")
    # Guess is higher than number
    elif guess > number:
        print("Too high!")
import random

while True:
    roll = input("Press enter to roll and press 0 to exit...") # Running the simulator until the user presses 0
    
    if roll == "0": # Ending the simulator if the user presses 0
        break
    else: # Outputting a dice roll if the user presses enter
        print(random.randint(1, 6))
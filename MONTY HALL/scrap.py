import random

# Generate a random number from 1 to 3 to represent the door with the prize
prize_door = random.randint(1, 3)

# Get the player's initial choice of door
player_choice = int(input("Pick a door (1, 2, or 3): "))

# Create a list of doors that are not the player's initial choice and do not contain the prize
other_doors = [door for door in range(1, 4) if door != prize_door and door != player_choice]

# Randomly reveal one of the other doors that does not contain the prize
revealed_door = random.choice(other_doors)

# Ask the player if they want to switch their choice to the other unopened door
switch_choice = input(f"The prize is not behind door {revealed_door}. Would you like to switch your choice to the other unopened door? (y/n): ")

# Determine the player's final choice of door based on their decision to switch or not
final_choice = player_choice
if switch_choice.lower() == 'y':
    final_choice = [door for door in range(1, 4) if door != player_choice and door != revealed_door][0]

# Print out the final result based on whether the player's final choice was correct or not
if final_choice == prize_door:
    print("Congratulations, you won the prize!")
else:
    print(f"Sorry, the prize was behind door {prize_door}. Better luck next time!")

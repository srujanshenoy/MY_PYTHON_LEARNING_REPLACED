import random

items = ['rock', 'paper', 'scissor']
computer_choice = random.choice(items)


def continue_game():
    usr_in = 'wrong'

    while usr_in.lower() not in ('y', 'n'):
        usr_in = input("Do you want to play again? (y/n)? ")

    usr_in = usr_in.lower()

    if usr_in == 'y':
        return True

    if usr_in == 'n':
        return False


continue_game_variable = True

while continue_game_variable:
    usr_in = input("What do you want to use? rock, paper or scissor? ")

    while usr_in.lower() not in items:
        usr_in = input("What do you want to use? rock, paper or scissor? ")

    usr_in = usr_in.lower()

    print(f"computer: {computer_choice}")
    print(f"You: {usr_in}")

    if computer_choice == 'rock':
        if usr_in == 'rock': print("You tied.")
        if usr_in == 'paper': print("You Won! :)")
        if usr_in == 'scissor': print("You lost. :(")

    if computer_choice == 'paper':
        if usr_in == 'rock': print("You lost. :( ")
        if usr_in == 'paper': print("You tied!")
        if usr_in == 'scissor': print("You Won. :)")

    if computer_choice == 'scissor':
        if usr_in == 'rock': print("You won :)")
        if usr_in == 'paper': print("You lost :(")
        if usr_in == 'scissor': print("You Tied.")

    continue_game_variable = continue_game()

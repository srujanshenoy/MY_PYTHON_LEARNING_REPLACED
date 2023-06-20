# from random import randint

# def roll(d: int):
#     """roll a dice with a given number of sides."""
#     return randint(0, d)

# def multi_roll(d: int):
#     """roll a number of dice."""
#     current_sum = 0
#     for i in range(d):
#         current_sum += roll(d)
#     return current_sum

# def int_input(prompt: str):
#     """get an integer from the user."""
#     while True:
#         try:
#             return int(input(prompt))
#         except ValueError:
#             print("Please enter an integer.")

# def continue_game():
#     """ask the user if they want to play again."""
#     usr_in = input("Press enter to continue. If not, press any key followed by enter to exit.")
#     if usr_in == "":
#         return True 
#     if usr_in.lower() != "":
#         return False

# def main():
#     """main function."""
#     continue_game_var = True
#     while continue_game_var:
#         print("Welcome to the dice roller.")
#         print("Please enter the number of dice you want to roll.")
#         num_dice = int_input("Number of dice: ")
#         print("Please enter the number of sides on each die.")
#         num_sides = int_input("Number of sides: ")
#         print(f"Rolling {num_dice} dice with {num_sides} sides each.")
#         print(f"The sum is {multi_roll(num_dice)}.")
#         continue_game_var = continue_game()

# if __name__ == "__main__":
#     main()


from random import randint

def roll(d: int):
    """roll a dice with a given number of sides."""
    return randint(1, d)

def multi_roll(d: int):
    """roll a number of dice."""
    current_sum = 0
    for i in range(d+1):
        current_sum += roll(d)
    return current_sum

def int_input(prompt: str):
    """get an integer from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter an integer.")

def continue_game():
    """ask the user if they want to play again."""
    usr_in = input("Press enter to continue. If not, press any key followed by enter to exit.")
    if usr_in == "":
        return True 
    if usr_in.lower() != "":
        return False

def main():
    """main function."""
    continue_game_var = True
    while continue_game_var:
        print("Welcome to the dice roller.")
        print("Please enter the number of dice you want to roll.")
        num_dice = int_input("Number of dice: ")
        print("Please enter the number of sides on each die.")
        num_sides = int_input("Number of sides: ")
        print(f"Rolling {num_dice} dice with {num_sides} sides each.")
        print(f"The sum is {multi_roll(num_dice)}.")
        continue_game_var = continue_game()

if __name__ == "__main__":
    main()
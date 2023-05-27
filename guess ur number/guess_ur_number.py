""" Guess Your Number - Normal Version / Main file"""


def slide_input(prompt) -> str:
    """
    Asks user Yes or No to the prompt.
    :param prompt: The prompt you want the user to respond Yes or No to.
    :return: String, '1' or '0'
    """
    usr_in = 'wrong'

    while usr_in.upper() not in ("Y", "N"):
        usr_in = input(prompt)

    if usr_in.upper() == "Y":
        usr_in = "1"

    if usr_in.upper() == "N":
        usr_in = "0"

    return usr_in


def continue_game() -> bool:
    """
    :return: boolean, Asks if they want to continue playing the game.
    """
    usr_in = 'wrong'

    while usr_in.upper() not in ("Y", "N"):
        usr_in = input("Keep Playing? Yes(y) or No(n)? ")

    if usr_in.upper() == 'Y':
        usr_in = True
        return usr_in

    if usr_in.upper() == 'N':
        print("Bye! Have a gr8 day!")
        usr_in = False
        return usr_in


CONTINUE_GAME_VAR = True

while CONTINUE_GAME_VAR:
    print("""
    Pick a nuber from 0 - 15
    If your number is there in a slide, type y for yes, 
    if not, type, n for no
    """)

    A = slide_input("slide 1: 1 3 5 7 9 11 13 15: ")
    B = slide_input("slide 2: 2 3 6 7 10 11 14 15: ")
    C = slide_input("slide 3: 4 5 6 7 12 13 14 15: ")
    D = slide_input("slide 4: 8 9 10 11 12 13 14 15: ")
    concatenated = D + C + B + A

    print(f"Your number is {int(concatenated, 2)}. ")

    CONTINUE_GAME_VAR = continue_game()

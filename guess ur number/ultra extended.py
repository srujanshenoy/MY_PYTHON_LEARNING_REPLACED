""" Improved version of extended guess ur number """

print("think of a number from 0 - 63\n"
      "If tour number is in a slide, than enter Y for Yes\n"
      "If not, N for No\n")


def usr_in_var(prompt) -> str:
    """Prompts usr input for slides"""

    while True:
        usr_in = input(prompt)

        if usr_in.upper() == 'Y':
            usr_in = "1"
            break

        if usr_in.upper() == "N":
            usr_in = "0"
            break

    return usr_in


def continue_game() -> bool:
    """Asks user if they want to continue the game"""

    usr_in = "wrong"

    while usr_in.lower() not in ('y', 'n'):

        usr_in = input("Do you want to continue? Yes(Y) or No(N)? ")
        if usr_in.lower() == 'y':
            return True
        if usr_in.lower() == 'n':
            return False


CONTINUE_GAM_VAR = True

while CONTINUE_GAM_VAR:
    X = usr_in_var("slide 1: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, \n"
                   "47, 49, 51, 53, 55, 57, 59, 61, 63: ")
    Y = usr_in_var("slide 2: 2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31, 34, 35, 38, 39, 42, 43, 46, \n"
                   "47, 50, 51, 54, 55, 58, 59, 62, 63: ")
    Z = usr_in_var("slide 3: 4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31, 36, 37, 38, 39, 44, 45, 46, \n"
                   "47, 52, 53, 54, 55, 60, 61, 62, 63: ")
    A = usr_in_var("slide 4: 8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31, 40, 41, 42, 43, 44, 45, \n"
                   "46, 47, 56, 57, 58, 59, 60, 61, 62, 63: ")
    B = usr_in_var("slide 5: 16, 17, 18, 19,20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 48, 49, 50, 51, 52, 53, \n"
                   "54, 55, 56, 57, 58, 59, 60, 61, 62, 63: ")
    C = usr_in_var("slide 6: 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, \n"
                   "54, 55, 56, 57, 58, 59, 60, 61, 62, 63: ")
    concatenated = C + B + A + Z + X + Y

    print(f"your number is {int(concatenated, 2)}")
    CONTINUE_GAM_VAR = continue_game()

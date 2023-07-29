def continue_game():
    usr_in = input("Do you want to continue? Press enter for yes and type anything and then press enter for no. ")
    if usr_in == '':
        return True

    return False

def add(a: float, b):
    return a + b

def float_input(prompt: str):
    usr_in = "wrong"

    while True:
        usr_in = input(prompt + " ")
        try:
            return float(usr_in)

        except ValueError:
            print("NaN error")



continue_game_variable = True

while continue_game_variable:
    a = float_input("a: ")
    b = float_input("b: ")

    print(add(a, b))

    continue_game_variable = continue_game()
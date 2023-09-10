def intinput(prompt: str):
    usr_in = "wrong"

    while True:
        usr_in = input(prompt + " ")
        try:
            return int(usr_in)
            break

        except ValueError:
            print("NaN error")
            
def continue_game():
    usr_in = input("Do you want to continue? Press enter for yes and type anything and then press enter for no. ")
    if usr_in == '':
        return True

    return False


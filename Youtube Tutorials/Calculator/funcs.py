def continue_game():
    """
    Asks the user if they want to continue, returns true/falase
    :return: bool
    """

    usr_in = "wrong"
    while usr_in.lower() not in ["y", "n"]:
        usr_in = input("Do you want to continue? [y / n]: ")

    output = True if usr_in.lower() == "y" else False
    return output

def float_input(prompt:str):
    """
    Takes user input as floating point value
    :param prompt: What to ask the user
    :return: float
    """
    while True:
        usr_in = input(prompt)
        try:
            return float(usr_in)

        except ValueError:
            continue


def operator_input():
    """
    Asks the user for an operator
    :return: str
    """

    usr_in = "wrong"
    while usr_in.lower() not in ["+", "-", "*", "/", "x", "X", ".", "^"]:
        usr_in = input("Operator [+ / - / x / ^ / /]: ")

    output = usr_in if usr_in in ['+', '-', '/', '^'] else 'x'
    return output

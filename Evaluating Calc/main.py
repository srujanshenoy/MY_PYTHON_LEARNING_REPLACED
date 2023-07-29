# Variables
result = 0
equation = "0 "

def opp_in():
    """ Asks for user input and checks to see if it is an operator """
    valid = ["+", "-", "x", "X", "*", "/", "="]
    while True:
        usr_in = input("operator (+, -, x, *, /, =(evaluate) ): ")
        if usr_in.lower() in valid:
            break
        else:
            pass

    return usr_in.lower()

def float_in(prompt: str):
    usr_in = "wrong"

    while True:
        usr_in = input(prompt + " ")
        try:
            return float(usr_in)

        except ValueError:
            print("NaN error")


while True:
    current_val = float_in("Number: ")
    opp = opp_in()

    if opp == "+":
        result += current_val
        equation += f" + {current_val}"

    if opp == "-":
        result -= current_val
        equation += f" - {current_val}"

    if opp.lower() == "x" or opp == "*":
        result *= current_val
        equation += f" x {current_val}"

    if opp == "/":
        result /= current_val
        equation += f" / {current_val}"

    if opp == "=":

        print(equation + " = " + str(result) + " (No order of operations) ")
        break

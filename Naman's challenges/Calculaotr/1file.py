from math import pow

cont = True


def intinput(prompt) -> int:
    """ takes a prompt and uses it to prompt the user to input a number. """
    while True:
        usr_in = input(prompt)
        try:
            usr_in = int(usr_in)
            break
        except:
            pass

    return usr_in


def operator_in() -> str:
    """ Asks the user to input an operator """
    valid = ["+", "-", "*", "/", "^"]
    while True:
        usr_in = input("operator (+, -, *, /, ^): ")
        if usr_in in valid:
            return usr_in


def continue_q():
    usr_in = input("Do you want to continue? yes(y) or no(n)?")
    if usr_in.lower() in ('y', 'n'):
        if usr_in.lower() == 'y':
            return True
        elif usr_in.lower() == 'n':
            return False
        else:
            continue_q()


def help():
    print("""
    This is a calculator. you can do 6 operations:
    + ==> add
    - ==> subtract
    * ==> multiply
    / ==> divide
    ^ ==> exponent

    for x and y, input any two numbers. for the operator, input any one of the above. 
    """)


while cont:
    help()

    number_1 = intinput("x: ")
    print(f"{number_1} _ y")
    operator = operator_in()
    print(f"{number_1} {operator} y")
    number_2 = intinput("y: ")
    print(f"{number_1} {operator} {number_2}")

    if operator == "+":
        print(f"{number_1} {operator} {number_2} = {number_1 + number_2}")

    elif operator == "-":
        print(f"{number_1} {operator} {number_2} = {number_1 - number_2}")

    elif operator == '*':
        print(f"{number_1} {operator} {number_2} = {number_1 * number_2}")

    elif operator == "/":
        print(f"{number_1} {operator} {number_2} = {number_1 / number_2}")

    elif operator == "^":
        print(f"{number_1} {operator} {number_2} = {pow(number_1, number_2)}")

    cont = continue_q()




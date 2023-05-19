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




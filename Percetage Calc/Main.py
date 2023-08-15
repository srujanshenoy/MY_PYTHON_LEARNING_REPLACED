"""
A calculator that helps calculate only percentages
"""

def float_input(prompt: str):
    """
    :param prompt: prompt for floating point input
    :return: float
    """
    usr_in = "wrong"

    while True:
        usr_in = input(prompt + " ")
        try:
            return float(usr_in)

        except ValueError:
            print("NaN error")


def programme_mode():
    usr_in = "wrong"

    while True:
        usr_in = input("""
        Enter a mode, 1 or 2.
        
        1. x% of y = __
        2. x is __% of y
        3. Quit
        """)

        if usr_in in ["1", "2", "3"]:
            return int(usr_in)


# Main loop
while True:
    mode = programme_mode()
    if mode == 1:
        print("x% of y = __")
        x = float_input("x: ")
        print(f"{x}% of y = __")
        y = float_input("y: ")
        print(f"{x}% of {y} = {x/100 * y}")

    if mode == 2:
        print("x is __% of y")
        x = float_input("x: ")
        print(f"{x} is __% of y")
        y = float_input("y: ")
        print(f"{x} is {(x*100)/y}% of y.")

    if mode == 3:
        break

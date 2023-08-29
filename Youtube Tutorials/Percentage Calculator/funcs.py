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
import math
import numpy as np

def continue_calc_question():
    print("Do you want to continue calculating? (y/n)")
    answer = input()
    if answer == 'y':
        return True
    else:
        return False

def float_input(prompt):
    while True:
        try:
            answer = float(input(prompt))
            return answer
        except ValueError:
            print("Please enter a number")

def logarithm(x, base):
    """
    Takes the logarithm of x to the base of base.

    Args:
        x: The number to take the logarithm of.
        base: The base of the logarithm.

    Returns:
        The logarithm of x to the base of base.
    """

    if base == 'e':
        return math.log(x)
    else:
        return np.log(x, base)

    if __name__ == "__main__":
        contnue_var = True
        while contnue_var:
            log_value = float_input("log _ to the base _: ")
            log_base = float_input(f"log {log_value} to the base _: ")
            print(logarithm(log_value, log_base))
            contnue_var = continue_calc_question()
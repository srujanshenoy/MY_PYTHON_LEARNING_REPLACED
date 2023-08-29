"""
A calculator that helps calculate only percentages
"""

from funcs import *

while True:
    mode = programme_mode()
    # Formula: 100x/y
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

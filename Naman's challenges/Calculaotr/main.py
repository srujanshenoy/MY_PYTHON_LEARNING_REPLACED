from funcs import *
from math import pow

cont = True

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




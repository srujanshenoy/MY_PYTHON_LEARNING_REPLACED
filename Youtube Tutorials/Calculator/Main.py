from funcs import *

continue_game_var = True

while continue_game_var:
    x = float_input("Value of x: ")
    opp = operator_input()
    y = float_input("Value of y: ")

    if opp == '+': print(x + y)
    if opp == '-': print(x - y)
    if opp == "x": print(x * y)
    if opp == "/": print(x / y)
    if opp == "^": print(x ** y)

    continue_game_var = continue_game()

from funcs import *

continue_game_var = True

while continue_game_var:
    print("""Welcome to the Fractions Calculator.""")
    Fraction_1 = fraction_input("numerator 1: ", "denominator 1: ")
    print(f"{Fraction_1.print()} (operator) (fraction 2)")
    operator = operator_input()
    print(f"{Fraction_1.print()} {operator} (fraction 2)")
    Fraction_2 = fraction_input("numerator 2: ", "denominator 2: ")
    print(f"{Fraction_1.print()} {operator} {Fraction_2.print()} \n")

    Paired = Fractional_operations(Fraction_1, Fraction_2)

    if operator == "+":
        Paired.add().print()
    
    elif operator == "-":
        Paired.subtract().print()

    elif operator == "/":
        Paired.divide().print()

    elif operator == "*":
        Paired.multiply().print()

    else: 
        print("somthing went wrong. Continuing...")

    continue_game_var = continue_game()

print("Thanks for playing!")

        




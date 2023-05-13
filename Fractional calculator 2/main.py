from funcs import *

quit_program = True

while quit_program:
    fraction_1 = Fraction(int_prompt("Numerator 1: "), int_prompt("Denominator 1: "))
    operator = operator_prompt()
    fraction_2 = Fraction(int_prompt("Numerator 2: "), int_prompt("Denominator 2: "))
    fraction_pair = FractionOperations(fraction_1, fraction_2)


    if operator == '+':
        Fraction.print_fraction(FractionOperations.add(fraction_pair))
    elif operator == '-':
        Fraction.print_fraction(FractionOperations.subtract(fraction_pair))
    elif operator == 'x':
        Fraction.print_fraction(FractionOperations.multiply(fraction_pair))
    elif operator == '/':
        Fraction.print_fraction(FractionOperations.divide(fraction_pair))
    else:
        print('somthing went wrong...')

    quit_program = input("Do you want to quit_program? Y / N: ")
    if quit_program.lower() == 'y':
        quit_program = False
    elif quit_program.lower() == 'n':
        quit_program = True


from fractionsfile import Fraction, Fractions, int_input, operator_input


numerator_1 = int_input("Enter numerator 1: ")
denominator_1 = int_input("Enter denominator 1: ")

numerator_2 = int_input("Enter numerator 2: ")
denominator_2 = int_input("Enter denominator 2: ")

fraction_1 = Fraction(numerator_1, denominator_1)
fraction_2 = Fraction(numerator_2, denominator_2)

operator = operator_input("Enter an operator (+, -, *, /): ")

fractions = Fractions(fraction_1, fraction_2)

if operator == "+": 
    print(Fracitons.add(Fractions))
if operator == "-": 
    print(Fracitons.subtract(Fractions))
if operator == "*": 
    print(Fracitons.multiply(Fractions))
if operator == "/": 
    print(Fracitons.divide(Fractions))

from fractionsfile import *
from fractionsfile import Fraction
from fractionsfile import Fractions 

Numerator1 = int_input("Enter the numerator of the first fraction: ")
Denominator1 = int_input("Enter the denominator of the first fraction: ")
operator = operator_input("Please enter an operator (+, -, *, /):")
Numerator2 = int_input("Enter the numerator of the second fraction: ")
Denominator2 = int_input("Enter the denominator of the second fraction: ")


Fraction1 = Fraction(Numerator1, Denominator1)
Fraction2 = Fraction(Numerator2, Denominator2)
Fractions_for_calculation = Fractions(Fraction1, Fraction2)

continue_game_var = True

while continue_game_var:
    if operator == '+': x = Fractions.add(Fractions_for_calculation)
    if operator == '-': x = Fractions.subtract(Fractions_for_calculation)
    if operator == '*': x = Fractions.multiply(Fractions_for_calculation)
    if operator == '/': x = Fractions.divide(Fractions_for_calculation)
    
    if x.numerator > x.denominator:
        print("Do you want the answer in a mixed fraction or an improper freaction?")
        mixed_or_improper = input("Enter m for mixed fraction and anything else for improper fraction: ")
        if mixed_or_improper == 'm': print(x.convert_to_mixed_fraction())
        else: print(x)
    
    continue_game_var = continue_game()
    
# End of code.
    
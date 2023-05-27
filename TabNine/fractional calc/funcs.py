from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def int_input(prompt):
    usr_in = 'wrong'
    while usr_in.isdigit() == False:
        usr_in = input(prompt)
    
    return int(usr_in)

def fraction_input(numerator_prompt, denominator_prompt):
    numerator = int_input(numerator_prompt)
    denominator = int_input(denominator_prompt)

    return Fraction(numerator, denominator)

def continue_game():
    usr_in = 'wrong'
    while usr_in.lower() not in ['y', 'n']:
        usr_in = input("Keep playing? (y/n): ")
        if usr_in.lower() == 'y':
            return True
        elif usr_in.lower() == 'n':
            return False

def operator_input() -> str:
    usr_in = 'wrong'
    while usr_in not in ['+', '-', '*', '/']:
        usr_in = input("Enter an operator (+, -, *, /): ")
    
    return usr_in

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def print(self):
        print(f"{self.numerator} / {self.denominator}")

class Fractional_operations:
    def __init__(self, fraction_1:Fraction, fraction_2:Fraction):
        self.fraction_1 = fraction_1
        self.fraction_2 = fraction_2

    def multiply(self):
        return \
        Fraction(
            self.fraction_1.numerator * self.fraction_2.numerator,
            self.fraction_1.denominator * self.fraction_2.denominator
        )

    def divide(self):
        return \
        Fraction(
            self.fraction_1.numerator * self.fraction_2.denominator,
            self.fraction_1.denominator * self.fraction_2.numerator
        )

    def add(self):
        output_denominator = gcd(self.fraction_1.denominator, self.fraction_2.denominator)
        multiplication_factor_fraction_1 = output_denominator / self.fraction_1.denominator
        multiplication_factor_fraction_2 = output_denominator / self.fraction_2.denominator
        return \
        Fraction(
            self.fraction_1.numerator * multiplication_factor_fraction_1 + self.fraction_2.numerator * multiplication_factor_fraction_2,
            output_denominator
        )
        
    def subtract(self):
        output_denominator = gcd(self.fraction_1.denominator, self.fraction_2.denominator)
        multiplication_factor_fraction_1 = output_denominator / self.fraction_1.denominator
        multiplication_factor_fraction_2 = output_denominator / self.fraction_2.denominator
        return \
        Fraction(
            self.fraction_1.numerator * multiplication_factor_fraction_1 - self.fraction_2.numerator * multiplication_factor_fraction_2,
            output_denominator
        )


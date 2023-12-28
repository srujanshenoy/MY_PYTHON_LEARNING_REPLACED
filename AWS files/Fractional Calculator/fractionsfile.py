import math

def int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            
            
def operator_input(prompt):
    while True:
        operator = input(prompt)
        if operator in ['+', '-', '*', '/']:
            return operator
        else:
            print("Invalid operator. Please enter a valid operator.")
            
def continue_game():
    while True:
        choice = input("Do you want to continue? Enter y for yes and anything else for no. ")
        if choice.lower() == 'y': return True
        return False
            
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def simplify(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd
        
    def convert_to_mixed_fraction(self):
        whole_number = self.numerator // self.denominator
        remainder = self.numerator % self.denominator
        return f"{whole_number} {remainder}/{self.denominator}"
    
        
        
class Fractions:
    def __init__(self, Fraction1: Fraction, Fraction2: Fraction):
        self.Fraction1 = Fraction1
        self.Fraction2 = Fraction2

    def add(self):
        numerator = self.Fraction1.numerator * self.Fraction2.denominator + self.Fraction2.numerator * self.Fraction1.denominator
        denominator = self.Fraction1.denominator * self.Fraction2.denominator
        result = Fraction(numerator, denominator)
        result.simplify()
        return result
    
    
    def subtract(self):
        numerator = self.Fraction1.numerator * self.Fraction2.denominator - self.Fraction2.numerator * self.Fraction1.denominator
        denominator = self.Fraction1.denominator * self.Fraction2.denominator
        result = Fraction(numerator, denominator)
        result.simplify()
        return result
    
    
    def multiply(self):
        numerator = self.Fraction1.numerator * self.Fraction2.numerator
        denominator = self.Fraction1.denominator * self.Fraction2.denominator
        result = Fraction(numerator, denominator)
        result.simplify()
        return result
    
    
    def divide(self):
        numerator = self.Fraction1.numerator * self.Fraction2.denominator
        denominator = self.Fraction1.denominator * self.Fraction2.numerator
        result = Fraction(numerator, denominator)
        result.simplify()
        return result
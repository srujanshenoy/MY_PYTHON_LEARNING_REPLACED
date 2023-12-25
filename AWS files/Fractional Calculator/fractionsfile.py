# A function to take the lcm of two numbers.

def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm

# a function to take the GCD of two numbers.

def gcd(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
    return gcd

def int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

def operator_input(prompt):
    while True:
        operator = input(prompt)
        if operator in ["+", "-", "*", "/"]:
            return operator
        else:
            print("Invalid input. Please enter a valid operator.")
            continue

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def simplify(self):
        hcf_is = gcd(self.numerator, self.denominator)
        self.numerator = self.numerator / hcf_is
        self.denominator = self.denominator / hcf_is
        return self

        whole_number = self.numerator // self.denominator
        self.numerator = self.numerator % self.denominator
        return whole_number, self.numerator, self.denominator

class Fractions:
    def __init__(self, fraction_1, fraction_2):
        self.fraction_1 = fraction_1
        self.fraction_2 = fraction_2

    def multiply(self):
        output = Fraction(self.fraction_1.numerator * self.fraction_2.numerator, self.fraction_1.denominator * self.fraction_2.denominator)
        return output

    def divide(self):
        output = Fraction(self.fraction_1.numerator * self.fraction_2.denominator, self.fraction_1.denominator * self.fraction_2.numerator)
        return output

    def add(self):
        output = Fraction.simplify(Fraction(self.fraction_1.numerator * self.fraction_2.denominator + self.fraction_2.numerator * self.fraction_1.denominator, self.fraction_1.denominator * self.fraction_2.denominator))
        return output

    def subtract(self):
        output = Fraction.simplify(Fraction(self.fraction_1.numerator * self.fraction_2.denominator - self.fraction_2.numerator * self.fraction_1.denominator, self.fraction_1.denominator * self.fraction_2.denominator))
        return output


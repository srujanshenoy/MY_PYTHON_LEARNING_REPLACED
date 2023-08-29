"""
Module for all functions used in the main.py file.
"""


def gcd(a, b):
    """Returns the greatest common divisor (GCD) of two numbers."""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Returns the least common multiple (LCM) of two numbers."""
    # Find the maximum of the two numbers
    max_num = max(a, b)

    # Keep incrementing the maximum number to find the LCM
    while True:
        if max_num % a == 0 and max_num % b == 0:
            return max_num
        max_num += 1


def int_prompt(prompt: str):
    """asks for user input and checks to see if it is an integer."""

    while True:
        usr_in = input(prompt)
        try:
            usr_in = int(usr_in)
            break
        except TypeError:
            pass

    return usr_in


def operator_prompt():
    """ Asks for user input and checks to see if it is an operator """
    valid = ["+", "-", "x", "/"]
    while True:
        usr_in = input("operator (+, -, x, /): ")
        if usr_in.lower() in valid:
            break
        else:
            pass

    return usr_in.lower()


class Fraction:
    """
    A class made for fractions and specifically the objects. Operations are
    written in class FractionOperations
    """

    def __init__(self, numerator: int, denominator: int) -> None:
        self.numerator = numerator
        self.denominator = denominator

    def simplify(self):
        """Simplifies any fraction into the simplest form"""

        hcf_is = gcd(self.numerator, self.denominator)
        # if self.denominator / hcf_is == 1:
        #     return self.numerator
        # else:
        #     return Fraction(self.numerator / hcf_is, self.denominator / hcf_is)
        return Fraction(self.numerator / hcf_is, self.denominator / hcf_is)


    def print_fraction(self):
        print(f"{int(self.numerator)} / {int(self.denominator)}")


class FractionOperations:
    """
    Takes 2 fractions and performs an operation on them.
    multiply, divide, add and subtract.
    """

    def __init__(self, fraction_1: Fraction, fraction_2: Fraction) -> None:
        self.fraction_1 = fraction_1
        self.fraction_2 = fraction_2

    def multiply(self):
        """
        returns a Fraction that is the product of two other fractions
        N1 * N2 / D1 * D2
        """
        return Fraction.simplify(
            Fraction(
                self.fraction_1.numerator * self.fraction_2.numerator,
                self.fraction_1.denominator * self.fraction_2.denominator,
            )
        )

    def divide(self):
        """
        Returns a Fraction that is the quotient of two fractions
        N1 * D2 / D1 * N2
        """
        return Fraction.simplify(
            Fraction(
                self.fraction_1.numerator * self.fraction_2.denominator,
                self.fraction_1.denominator * self.fraction_2.numerator,
            )
        )

    def add(self):
        """ Adds any two fractions. """
        lcm_denominators = lcm(self.fraction_1.denominator, self.fraction_2.denominator)
        multiplication_coefficient_1 = lcm_denominators / self.fraction_1.denominator
        multiplication_coefficient_2 = lcm_denominators / self.fraction_2.denominator
        additive_numerator_1 = self.fraction_1.numerator * multiplication_coefficient_1
        additive_numerator_2 = self.fraction_2.numerator * multiplication_coefficient_2
        return Fraction.simplify(Fraction(additive_numerator_1 + additive_numerator_2, lcm_denominators))

    def subtract(self):
        """Subtracts any two given fractions."""
        lcm_denominators = lcm(self.fraction_1.denominator, self.fraction_2.denominator)
        multiplication_coefficient_1 = lcm_denominators / self.fraction_1.denominator
        multiplication_coefficient_2 = lcm_denominators / self.fraction_2.denominator
        subtractive_numerator_1 = self.fraction_1.numerator * multiplication_coefficient_1
        subtractive_numerator_2 = self.fraction_2.numerator * multiplication_coefficient_2
        return Fraction.simplify(Fraction(subtractive_numerator_1 - subtractive_numerator_2, lcm_denominators))

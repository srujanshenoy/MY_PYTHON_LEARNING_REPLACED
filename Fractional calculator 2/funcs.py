"""
Module for all functions used in the main.pY file.
"""


def hcf(a, b):
    "Returns the HCF or GCD of any two integers."
    if b == 0:
        return abs(a)
    else:
        return hcf(b, a % b)


class Fraction:
    """
    A class made for fractions and spesifically the objects. Operations are
    written in class FractionOperations
    """

    def __init__(self, numerator: int, denominator: int) -> None:
        self.numerator = numerator
        self.denominator = denominator

    def simplify(self):
        "Simplifies any fraction into simplest form"
        hcf_is = hcf(self.numerator, self.denominator)
        return Fraction(self.numerator / hcf_is, self.denominator / hcf_is)


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
        Returns a Fraction that is the qutient of two fractions
        N1 * D2 / D1 * N2
        """
        return Fraction.simplify(
            Fraction(
                self.fraction_1.numerator * self.fraction_2.denominator,
                self.fraction_1.denominator * self.fraction_2.numerator,
            )
        )

    def add(self):
        "Adds any two given fractions."
        hcf_denominators = hcf(self.fraction_1.denominator, self.fraction_2.denominator)
        # adjust numerators to equalize denominators
        numerator_1 = self.fraction_1.numerator * hcf_denominators
        numerator_2 = self.fraction_2.numerator * hcf_denominators

        return Fraction.simplify(Fraction(numerator_1 + numerator_2, hcf_denominators))

    def subtract(self):
        "Subtracts any two given fractions."
        hcf_denominators = hcf(self.fraction_1.denominator, self.fraction_2.denominator)
        # adjust numerators to equalize denominators
        numerator_1 = self.fraction_1.numerator * hcf_denominators
        numerator_2 = self.fraction_2.numerator * hcf_denominators

        return Fraction.simplify(Fraction(numerator_1 - numerator_2, hcf_denominators))

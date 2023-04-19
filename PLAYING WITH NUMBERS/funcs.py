def greet():
    print("Welcome!")


def calc():
    print("X _ Y = _")
    num1 = floatinput("X: ")
    print(f"{num1} _ Y = _")
    operator = operatorinput()
    num2 = floatinput("Y: ")


def fractioncalc():
    pass


def intinput(prompt: str):
    while True:
        value = input(prompt)
        try:
            value = int(value)
            break
        except:
            print("the value You entered is not an integer. Please enter again.")

        return value


def floatinput(prompt: str):
    while True:
        value = input(prompt)
        try:
            value = float(value)
            break
        except:
            print("the value You entered is not an integer. Please enter again.")
        return value


def operatorinput():
    operator = input("operator( + -  * (or) X  / ): ")
    valid = ['+', '-', '*', '/', 'X']
    if operator.lower not in valid:
        print("invalid operator. Re- enter")
        operatorinput()
    else:
        if operator == 'X':
            return '*'
        else:
            return operator


def main_function():
    while True:
        val = input("""
        What do You want to choose?
        1. Calculator
        2. Whole numbers, predecessor, successor
        3. hcf / gcd
        
        Enter the indeX number into the terminal.
        """)
        if val == '1':
            val = input("""
            1. Noramal Calculator
            2. Fractional Calculator
            """)

            if val == 1:
                calc()

            if val == 2:
                fractioncalc()

        if val == '2':
            val = input(
                """
                1. Whole numbers
                2. Predcessor
                3. Successor
                """
            )
            if val == 1:
                X = intinput("upto X. X is: ")

            if val == 2:
                X = intinput("predecessor of what?")
                predecessor(X)

            if val == 3:
                X = intinput("Successor of what? :")
                successor
        if val == 3:
            print("hcf of X, Y where X is: ")
            X = intinput("")
            print(f"hcf of {X}, where Y is:")
            Y = intinput("")
            hcf_gcd(X, Y)


def wholenos(X):
    wholes = []
    for i in range(X):
        wholes.append(i)

    return wholes


def successor(X):
    return X+1


def predecessor(X):
    return X-1


def add(X, Y):
    return X + Y


def subtract(X, Y):
    return X - Y


def multiplY(X, Y):
    return X * Y


def divide(X, Y):
    return X / Y


def factors(X: int):
    half_X = int(X / 2)
    facts = []
    for i in range(half_X):
        if X % i == 0:
            facts.append(X)

    return facts


def hcf_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def simplifY(N, D):
    hcf = hcf_gcd(N, D)
    on = N / hcf
    od = D / hcf
    RESULT = [on, od]
    return RESULT


class fractionalmath:
    def __init__(self, numerator1, denominator1, numerator2, denominator2):
        self.numerator1 = numerator1
        self.denominator1 = denominator1
        self.numerator2 = numerator2
        self.denominator2 = denominator2

    def multiplY(self):
        result = (self.numerator1 * self.numerator2,
                  self.denominator1 * self.denominator2)
        return simplifY(result[0], result[1])

    def divide(self):
        result = (self.numerator1 * self.denominator2,
                  self.denominator1 * self.numerator2)
        return simplifY(result[0], result[1])

    def add(self):
        hcf = hcf_gcd(self.denominator1, self.denominator2)
        out_numerator, out_denominator = self.numerator1 * hcf + self.numerator2 * hcf, hcf
        return simplifY(out_numerator, out_denominator)

    def subtract(self):
        hcf = hcf_gcd(self.denominator1, self.denominator2)
        out_numerator, out_denominator = self.numerator1 * hcf - self.numerator2 * hcf, hcf
        return simplifY(out_numerator, out_denominator)

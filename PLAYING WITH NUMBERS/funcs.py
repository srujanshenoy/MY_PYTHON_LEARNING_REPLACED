def greet():
    print("Welcome!")


def calc():
    pass


def fractioncalc():
    pass


def intinput(prompt: str):
    while True:
        value = input(prompt)
        try:
            value = int(value)
            break
        except:
            print("the value you entered is not an integer. Please enter again.")
        return value


def main_function():
    while True:
        val = input("""
        What do you want to choose?
        1. Calculator
        2. Whole numbers, predecessor, successor
        3. hcf / gcd
        
        Enter the index number into the terminal.
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
                x = intinput("upto x. x is: ")

            if val == 2:
                x = intinput("predecessor of what?")
                predecessor(x)

            if val == 3:
                x = intinput("Successor of what? :")
                successor
        if val == 3:
            print("hcf of x, y where x is: ")
            x = intinput("")
            print(f"hcf of {x}, where y is:")
            y = intinput("")
            hcf_gcd(x, y)


def wholenos(x):
    wholes = []
    for i in range(x):
        wholes.append(i)

    return wholes


def successor(x):
    return x+1


def predecessor(x):
    return x-1


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def factors(x: int):
    half_x = int(x / 2)
    facts = []
    for i in range(half_x):
        if x % i == 0:
            facts.append(x)

    return facts


def hcf_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def simplify(N, D):
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

    def multiply(self):
        result = (self.numerator1 * self.numerator2,
                  self.denominator1 * self.denominator2)
        return simplify(result[0], result[1])

    def divide(self):
        result = (self.numerator1 * self.denominator2,
                  self.denominator1 * self.numerator2)
        return simplify(result[0], result[1])

    def add(self):
        hcf = hcf_gcd(self.denominator1, self.denominator2)
        out_numerator, out_denominator = self.numerator1 * hcf + self.numerator2 * hcf, hcf
        return simplify(out_numerator, out_denominator)

    def subtract(self):
        hcf = hcf_gcd(self.denominator1, self.denominator2)
        out_numerator, out_denominator = self.numerator1 * hcf - self.numerator2 * hcf, hcf
        return simplify(out_numerator, out_denominator)

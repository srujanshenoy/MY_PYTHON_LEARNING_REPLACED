def sqrt(x: float):
    return x ** 0.5


class Triangle:
    def __init__(self, side_a: float, side_b: float, side_c: float, height: float = None, base: float = None):
        a = self.a = side_a
        b = self.b = side_b
        c = self.c = side_c
        self.right = True if a ** 2 + b ** 2 == c ** 2 else False
        h = self.height = self.a if self.right else (height if height != None else "Not provided")
        b = self.breadth = self.b if self.right else (base if base != None else "Not provided")
        self.hypotenuse = side_c

        # TRIGONOMETRIC FUNCTIONS

        self.sin = a / c if self.right else "Does not exist(Not a right triangle)"
        self.cos = b / c if self.right else "Does not exist(Not a right triangle)"
        self.tan = a / b if self.right else "Does not exist(Not a right triangle)"

        self.csc = 1 / self.sin if self.right else "Does not exist(Not a right triangle)"
        self.sec = 1 / self.cos if self.right else "Does not exist(Not a right triangle)"
        self.cot = 1 / self.tan if self.right else "Does not exist(Not a right triangle)"

        # Area - Heron's formula

        s = semiperimeter = (a + b + c) / 2
        self.area = sqrt(s * (s - a) * (s - b) * (s - c))

def side_input(side):
    while True:
        usr_in = input(f"side {side}: ('-' not permitted): ")
        try:
            if usr_in == '-': continue
            if usr_in != '-':
                return int(usr_in)

        except: continue



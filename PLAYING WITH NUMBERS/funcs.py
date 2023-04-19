def greet():
    print("Welcome!")

def calc():
    pass
def enter_val():
    val = input("""
    What do you want to choose?
    1. Calculator
    2. Whole numbers, predecessor, successor
    3. hcf / gcd
    
    Enter the index number into the terminal.
    """)
    if val == 1:
        calc()
    if val == 2:
        val =  input(
            """
            
            """
        )

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
    factors = []
    for i in range(half_x):
        if x % i == 0:
            factors.append(x)

    return factors

def hcf_gcd(a, b):
       while b != 0:
            a, b = b, a % b
       return a




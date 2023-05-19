def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ^ y

def float_check(prompt: str):
    while True:
        usr_in = input(prompt)
        try:
            usr_in = float(usr_in)
        except Exception:
            pass





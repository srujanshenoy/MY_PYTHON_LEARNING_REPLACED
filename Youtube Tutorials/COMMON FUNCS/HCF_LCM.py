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

def primes(n):
    """
    Returns a list of prime numbers up to n using the trial division method.
    """
    primes = [2] # initialize the list of primes with 2, the first prime number
    for i in range(3, n+1, 2): # iterate over odd numbers from 3 to n
        is_prime = True # assume the number is prime until proven otherwise
        for j in range(2, int(i**0.5)+1): # check if the number is divisible by any smaller prime number
            if i % j == 0:
                is_prime = False
                break
        if is_prime: # if the number is prime, add it to the list
            primes.append(i)
    return primes

# print(primes(100))

def generate_coprimes(n):
    """
    Returns a list of pairs of coprime integers up to n.
    """
    coprimes = []
    for i in range(2, n+1):
        for j in range(i+1, n+1):
            if gcd(i, j) == 1:
                coprimes.append((i, j))
    return coprimes

def gcd(a, b):
    """
    Returns the greatest common divisor of a and b using the Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a

# print(generate_coprimes(100))

def pairs(x):
    nums = list(range(0, x + 1))  # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...
    nth_element = 1
    modulo_number = nums[nth_element]
    count = 0
    coprime_pairs = []
    for i in nums:
        if i % modulo_number == 0 and count < 5:
            coprime_pairs.append((i, modulo_number))
            nth_element += 1
            count += 1
            i -= 1
        else:
            pass

        return coprime_pairs

print(pairs(20))




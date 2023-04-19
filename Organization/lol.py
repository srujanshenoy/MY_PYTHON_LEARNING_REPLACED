def primes(x):
    numbers = list(range(2, x))
    prime_numbers = []
    for number in numbers:
        prime_numbers.append(number)

    lesser_numbers = list(range(0))

    for number in numbers:
        lesser_numbers = list(range(2, number))
        for i in lesser_numbers:
            if number % i == 0:
                prime_numbers.remove(i)

        return prime_numbers

print(primes(100))

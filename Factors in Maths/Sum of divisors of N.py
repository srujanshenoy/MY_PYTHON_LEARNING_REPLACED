def sum_divisors(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)

def intinput(prompt: str):
    usr_in = "wrong"

    while True:
        usr_in = input(prompt + " ")
        try:
            return int(usr_in)
            break

        except ValueError:
            print("NaN error")

number = intinput("Number to find Sum of divisors for: ")
print(sum_divisors(number))
# print(prime_factors(16))

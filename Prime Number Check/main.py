def sqrt(x):
	return x ** 0.5

def check_prime(number: int):
    if number < 2:
        return False

    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


def int_input(prompt: str):
    usr_in = "wrong"

    while True:
        usr_in = input(prompt + " ")
        try:
            return int(usr_in)

        except ValueError:
            print("NaN error")

usr_in = int_input("Number for prime check:")
if check_prime(usr_in) == True: print(f"{usr_in} is prime.")
if check_prime(usr_in)== False: print(f"{usr_in} is not prime.")


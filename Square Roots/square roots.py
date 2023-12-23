from math import sqrt as sqrt 

def intinput(prompt: str):
    usr_in = "wrong"

    while True:
        usr_in = input(prompt + " ")
        try:
            return int(usr_in)

        except ValueError:
            print("NaN error")

number = intinput("Number:")
square_root = sqrt(number)

print(f"The square root of {number} is {square_root}")

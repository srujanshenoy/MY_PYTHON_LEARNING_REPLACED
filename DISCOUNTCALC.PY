amount = float(input("amount: "))
discount = float(input("discount:(do not type percent symbol) "))
print(f"{discount} % ")

# amount - (amount * discount/100)
step_1 = amount * discount/100
step_2 = amount - step_1
print(f"your end result is {step_2}")

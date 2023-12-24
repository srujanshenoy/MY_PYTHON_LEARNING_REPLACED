# CALCULATOR

def int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def operator_input(prompt):
    while True:
        operator = input(prompt)
        if operator in ['+', '-', '*', '/']:
            return operator
        else:
            print("Invalid operator. Please enter +, -, *, or /.")

def continue_input(prompt):
    while True:
        choice = input(prompt)
        if choice.lower() in ['y', 'n']:
            return choice.lower() == 'y'
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

continue_calculation = True
cycle_count = 0
result = 0

while continue_calculation:
    num1 = int_input("Enter the first number: ") if cycle_count == 0 else result
    operator = operator_input("Enter the operator (+, -, *, or /): ")
    num2 = int_input("Enter the second number: ")
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    print(f"The result is {result}.")

    continue_calculation = continue_input("Do you want to continue? (y/n): ")
    cycle_count += 1
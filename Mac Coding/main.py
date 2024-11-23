def int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")


def float_input(prompt):
    while True:
        try:
            usr_in = input(prompt)
            if usr_in == "//":
                return "Break"
            else:
                return float(usr_in)

        except ValueError:
            print("Invalid input. Please enter a number.")

def operator_input(prompt):
    while True:
        operator = input(prompt)
        if operator in ['+', '-', '*', '/']:
            return operator
        else:
            print("Invalid input. Please enter a valid operator.")

def continue_q(): return not input("Do you want to continue? (_ for yes and anything else for no.)")

def calc(starting:bool, current_value):
    continue_var = True
    while continue_var:
        print(f"Current value: {current_value}")
        num1 = float_input("Enter the first number: ") if starting else current_value
        operator = operator_input("Enter the operator: ")
        num2 = float_input("Enter the second number: ") if starting else float_input("Enter the number: ")

        match operator:
            case '+':
                current_value = num1 + num2
            case '-':
                current_value = num1 - num2
            case '*':
                current_value = num1 * num2
            case '/':
                current_value = num1 / num2
            case _:
                print("Invalid operator")
                return

        continue_var = continue_q()
        if continue_var:
            calc(False, current_value)

calc(True, 0)
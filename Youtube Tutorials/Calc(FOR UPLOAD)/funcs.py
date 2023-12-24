def int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def opertaor_input(prompt):
    while True:
        operator = input(prompt)
        if operator in ['+', '-', '*', '/']:
            return operator
        else:
            print("Invalid operator. Please enter a valid operator.")

def continue_calculation():  # Function to ask the user if they want to continue calculating. Returns True if they want to continue, False if they want to exit.
    while True:
        choice = input("Do you want to continue calculating? (y/n): ")
        if choice in ['y', 'n']:
            return choice == 'y'
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")


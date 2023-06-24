import math

def continue_calc_question():
    print("Do you want to continue calculating? (y/n)")
    answer = input()
    if answer == 'y':
        return True
    else:
        return False

def float_input(prompt):
    while True:
        try:
            answer = float(input(prompt))
            return answer
        except ValueError:
            print("Please enter a number")

def calculate_logarithm(base, n):
    """
    This function takes two numbers as arguments and returns the logarithm of n to the base of base.
    
    Parameters:
    base (float): The base of the logarithm
    n (float): The number to be logged
    
    Returns:
    float: The logarithm of n to the base of base
    """
    try:
        # Check if both arguments are numbers
        if not isinstance(base, (int, float)) or not isinstance(n, (int, float)):
            raise TypeError("Both arguments must be numbers")
        
        # Calculate and return the logarithm
        return math.log(n, base)
    except ValueError as e:
        # Log the error
        print(f"Error: {e}")
        return 0

    if __name__ == "__main__":
        contnue_var = True
        while contnue_var:
            log_value = float_input("log _ to the base _: ")
            log_base = float_input(f"log {log_value} to the base _: ")
            print(calculate_logarithm(log_value, log_base))
            contnue_var = continue_calc_question()


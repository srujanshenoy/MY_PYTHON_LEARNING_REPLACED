def int_input(prompt) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

def operator_input() -> str:
    usr_in = 'wrong'
    while usr_in not in ['+', '-', '*', '/', "^"]:
        usr_in = input("Enter an operator (+, -, *, /, ^): ")
    
    return usr_in

def continue_game():
    usr_in = 'wrong'
    while usr_in.lower() not in ['y', 'n']:
        usr_in = input("Do you want to continue? (y/n): ")
    
    if usr_in.lower() == 'y':
        return True
    
    else:
        return False
    

continue_game_var = True

while continue_game_var:
    print("Welcome to the calculator!")
    num_1 = int_input("Enter first number: ")
    operator = operator_input()
    num_2 = int_input("Enter second number: ")

    if operator == '+':
        print(num_1 + num_2)

    if operator == '-':
        print(num_1 - num_2)

    if operator == '*':
        print(num_1 * num_2)

    if operator == '/':
        print(num_1 / num_2)

    if operator == '^':
        print(num_1 ** num_2)

    continue_game_var = continue_game()
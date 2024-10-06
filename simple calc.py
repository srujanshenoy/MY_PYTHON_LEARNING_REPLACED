def float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("NaN. Enter an ACTUAL number")

def opp_in():
    usr_in = input("Enter an Opperator: ")
    if usr_in in ['+', '-', 'x', '/']: return usr_in
    else: return opp_in()

def main():
    number_1 = float_input("Enter the first no.: ")
    opperator = opp_in()
    number_2 = float_input("Enter the second no.: ")

    if opperator == '+': print(number_1 + number_2)
    if opperator == '-': print(number_1 - number_2)
    if opperator == 'x': print(number_1 * number_2)
    if opperator == "/": print(number_1 / number_2)

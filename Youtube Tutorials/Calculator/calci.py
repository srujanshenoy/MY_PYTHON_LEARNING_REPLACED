def float_input(prompt: str): 
    while True:
        try: return float(input(prompt))
        except Exception: pass

def opp_input(): 
    while True:
        usr_in = input("enter an opperator: ")
        if usr_in in ["+", "-", "*", "/", "**", "^"]: return usr_in
        else: print("invalid operator")

def main():
    i = 0

    while True:
        
        num1 = float_input("enter first number: ") if i == 0 else result
        opp = opp_input()
        num2 = float_input("enter second number: ")

        if opp == "+":
            result = (num1 + num2)
        elif opp == "-":
            result = (num1 - num2)
        elif opp == "*":
            result = (num1 * num2)
        elif opp == "/":
            if num2 == 0: 
                print("cannot divide by 0")
                break

            else: 
                result = (num1 / num2)

        elif opp == "**" or opp == "^":
            try: result = (num1 ** num2)
            except OverflowError: print("result too large, plz continue w/o this opperation")
            continue


        print(result)

        i += 1
        



if __name__ == "__main__":
    main()

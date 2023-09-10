INT_TO_TALLY = {0: "  ", 1: "|  ", 2: "| |  ", 3: "| | |  ", 4: "| | | |  ", 5: "-|-|-|-|-  "}

def convert_to_tally(integer: int) -> str:
    return str((INT_TO_TALLY[5])*int(integer/5)) + INT_TO_TALLY[integer % 5]


def intinput(prompt):
    while True:
        usr_in = input(prompt)
        try   : return int(usr_in)
        except: pass

print(convert_to_tally(intinput("Convert ___ to tally: ")))

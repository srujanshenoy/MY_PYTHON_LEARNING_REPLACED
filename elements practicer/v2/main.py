elements = {
    "H": ("Hydrogen", 1),
    "He": ("Helium", 2),
    "Li": ("Lithium", 3),
    "Be": ("Beryllium", 4),
    "B": ("Boron", 5),
    "C": ("Carbon", 6),
    "N": ("Nitrogen", 7),
    "O": ("Oxygen", 8),
    "F": ("Fluorine", 9),
    "Ne": ("Neon", 10)
}


def process_input(user_input):
    command, value = user_input.split(" ", 1)

    if command == "S":
        element = elements.get(value)
        if element:
            print(f"{element[1]}, {element[0]}")
        else:
            print("Element not found.")

    elif command == "n":
        for symbol, (name, number) in elements.items():
            if number == int(value):
                print(f"{symbol}, {name}")
                break
        else:
            print("Element not found.")

    elif command == "N":
        for symbol, (name, number) in elements.items():
            if name == value:
                print(f"{symbol}, {number}")
                break
        else:
            print("Element not found.")

    else:
        print("Invalid command.")


# # Test the function
# process_input("S H")
# process_input("N 1")
# process_input("E Hydrogen")
# process_input(input())

print("""
S (Symbol)
N (Element name)
n (Atomic number)

command lookup
""")

while True:
    usr_input = input(">>>")
    process_input(usr_input)



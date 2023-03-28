def vprint(characters:str):
    for char in characters:
        print(char)


# mainloop
while True:
    string_1 = input("type anything...")
    vprint(string_1)

    choice = input("Do you want to go again?\n"
                   "if yes, type 1\n"
                   "if no, type anything else >>")

    if choice == '1':
        continue
    elif choice == '2':
        break
    else:
        break
def int_input(prompt):
    usr_in = "wrong"
    while False == usr_in.isdigit():
        usr_in = input(prompt)

    return int(usr_in)

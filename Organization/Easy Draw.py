import turtle

pen = turtle.Turtle()

print("""

Command format: {command} {distance / angle}

Commands:
    1. fd => moves turtle forward
    2. bk => moves turtle backward
    3. rt => turns turtle right by {x} degrees
    4. lt => turns turtle left by {x} degrees
    5. stop => stops program
""")

def command_in():
    """ asks the user to input a command """
    usr_in = 'wrong'
    valid = ['fd', 'bk', 'rt', 'lt', 'stop']
    while usr_in not in valid:
        usr_in = input("enter a command... ")
        if usr_in.lower() in valid:
            break

    return usr_in.lower()



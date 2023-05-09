import os

type_of_in = input("text or file?? input as written in question: ")
if type_of_in.lower() == 'text':
    hiding_spot = input("Where do you want to hide your text? provide full location: ")
    extention = input("Stream name: ")
    print("please type your secret text in the above window. press enter when done.")
    os.system(f"notepad {hiding_spot}:{extention}")
    wait = input(">>> ")
    if type(wait) != int:
        print(f"""
        Done!
        you can access your secret text with this command in cmd:
        notepad {hiding_spot}:{extention}
        """)
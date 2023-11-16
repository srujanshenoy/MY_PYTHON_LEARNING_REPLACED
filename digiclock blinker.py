from tkinter import *
from tkinter.ttk import *
from time import strftime

window = Tk()
window.title("Clock")

def changeLabel():
    time2 = strftime('%I:%M %p')
    if ':' in time2:
        time2 = time2.replace(':', ' ')
    else:
        time2 = time2.replace(' ', ':')
    label.config(text=time2)
    label.after(1000, changeLabel)

label = Label(window, font=("Arial", 60), background="black", foreground="magenta")
label.pack(anchor="center")
changeLabel()

window.mainloop()

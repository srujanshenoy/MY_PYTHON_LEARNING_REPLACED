from tkinter import *
from tkinter.ttk import *
from time import strftime

window = Tk()
window.title("Clock")

def time():
    # string = strftime("%I:%M:%S %p")
    # string = strftime("%I:%M")
    string = strftime("%I:%M %p")
    label.config(text=string)
    label.after(1000, time)

label = Label(window, font=("Arial", 60), background="black", foreground="magenta")
label.pack(anchor="center")
time()

window.mainloop()
import tkinter as tk

global calculation

def add_to_calculation(value):
    global calculation
    calculation = ""
    calculation += value
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()



def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")



root = tk.Tk()

root.geometry("300x275")

text_result = tk.Text(height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

btn_1 = tk.Button(root, text=1, command=lambda: add_to_calculation(1), width=5, font=('Arial', 18))
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root, text=1, command=lambda: add_to_calculation(2), width=5, font=('Arial', 18))
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root, text=1, command=lambda: add_to_calculation(3), width=5, font=('Arial', 18))
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text=1, command=lambda: add_to_calculation(4), width=5, font=('Arial', 18))
btn_4.grid(row=2, column=1)

btn_5 = tk.Button(root, text=1, command=lambda: add_to_calculation(5), width=5, font=('Arial', 18))
btn_5.grid(row=2, column=1)

btn_6 = tk.Button(root, text=1, command=lambda: add_to_calculation(6), width=5, font=('Arial', 18))
btn_6.grid(row=2, column=1)

btn_7 = tk.Button(root, text=1, command=lambda: add_to_calculation(7), width=5, font=('Arial', 18))
btn_7.grid(row=2, column=1)

btn_8 = tk.Button(root, text=1, command=lambda: add_to_calculation(8), width=5, font=('Arial', 18))
btn_8.grid(row=2, column=1)

btn_9 = tk.Button(root, text=1, command=lambda: add_to_calculation(9), width=5, font=('Arial', 18))
btn_9.grid(row=2, column=1)

btn_0 = tk.Button(root, text=1, command=lambda: add_to_calculation(0), width=5, font=('Arial', 18))
btn_0.grid(row=2, column=1)


root.mainloop()






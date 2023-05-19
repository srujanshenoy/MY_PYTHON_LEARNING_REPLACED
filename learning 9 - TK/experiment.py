import tkinter as tk
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.configure(bg='#cecece')
        self.window.title('My experiments with truth')
        self.window.colormapwindows()

        self.entry = tk.Entry()

        self.text1 = tk.Text(height = 1, font=('Arial', 18))
        self.text1.pack(padx=10, pady=10)

        self.textbox = tk.Text(height=3, font=('Arial', 16), borderwidth=3.0, background="#dedede")
        self.textbox.pack(padx=10, pady=10)

        self.checkinfo = tk.Button(text="SHOW INFO BOX", font=('Arial', 18), command=self.show_info_message)
        self.checkinfo.pack(padx=10, pady=10)

        self.checkerror = tk.Button(text="SHOW ERROR BOX", font=('Arial', 18), command=self.show_error_message)
        self.checkerror.pack(padx=10, pady=10)

        self.checkwarrning = tk .Button(text="SHOW WARNING BOX", font=('Arial', 18), command=self.show_warning_message)
        self.checkwarrning.pack(padx=10, pady=10)

        self.window.mainloop()

    def show_info_message(self):
        messagebox.showinfo(title=self.text1.get('1.0', tk.END), message=self.textbox.get('1.0', tk.END))

    def show_error_message(self):
        messagebox.showerror(title=self.text1.get('1.0', tk.END), message=self.textbox.get('1.0', tk.END))

    def show_warning_message(self):
        messagebox.showwarning(title=self.text1.get('1.0', tk.END), message=self.textbox.get('1.0', tk.END))

MyGUI()
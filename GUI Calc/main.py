import tkinter as tk

# Function to update the display when a button is clicked or a key is pressed
def update_display(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# Function to clear the display
def clear_display():
    entry.delete(0, tk.END)

# Function to calculate the result
def calculate():
    current = entry.get()
    try:
        result = eval(current)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry widget for the display
entry = tk.Entry(root, width=20, font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for the calculator
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', 'x',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 20), command=calculate).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 20), command=lambda button=button: update_display(button)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Bind keyboard events
root.bind('<Key>', lambda event: update_display(event.char))
root.bind('<Return>', lambda event: calculate())
root.bind('<Escape>', lambda event: clear_display())

# Run the GUI main loop
root.mainloop()
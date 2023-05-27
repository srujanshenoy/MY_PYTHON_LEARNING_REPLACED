from funcs import *
import prettytable
import tkinter as tk
from tkinter import ttk

from_value = int_input("from tables: ")
to_value = int_input("to tables: ")
tables_table = prettytable.PrettyTable(border=True, border_width='2')
tables_table.border_style = 'outset'

for table in range(from_value, to_value):
    append_list = []
    for x_what in range(1, 11):
        # print(f"{table} x {x_what} = {table * x_what}")
        append = str(table) + "x" + str(x_what) + "=" + str(table * x_what)
        append_list.append(append)

    tables_table.add_column(str(table), append_list)

print(tables_table)

# """ #TKINTER """
#
# window = tk.Tk()
# window.geometry("600x400")
#
# # text = tk.Label(text=str(tables_table), font=('Arial', 18))
# # text.pack()
#
# Table = ttk.Treeview()
# Table.pack()
#
#
# window.mainloop()
#

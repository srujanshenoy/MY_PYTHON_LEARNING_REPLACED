from funcs import *
from tabulate import tabulate

from_value = int_input("from tables: ")
to_value = int_input("to tables: ")
tables_table =[]
tables_dict = {}

for table in range(from_value, to_value):
    append_list = [table]
    table_headers = []
    for x_what in range(1, 11):
        table_headers.append('x' + str(x_what))
        # print(f"{table} x {x_what} = {table * x_what}")
        append = str(table) + "x" + str(x_what) + "=" + str(table * x_what)
        append_list.append(append)

    tables_table.append(append_list)



print(tabulate(tables_table, headers=table_headers,tablefmt="fancy_grid"))
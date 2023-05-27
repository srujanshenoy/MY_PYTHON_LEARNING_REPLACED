from tabulate import tabulate

table_data = [['Name', 'Age', 'Job'],
              ['Mike', 22, 'Programmer'],
              ['John', 23, 'Teacher'],
              ['Jane', 23, 'Designer'],
              ['Jack', 25, 'Manager'],
              ['Jill', 26, 'Programmer'],
              ['John', 27, 'Student'],
              ['Mike', 28, 'Driver']]

print(tabulate(table_data, headers=['Name', 'Age', 'Job'], tablefmt="fancy_grid"))





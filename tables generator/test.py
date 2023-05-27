import prettytable

table = prettytable.PrettyTable(border=True, border_width=100)
table.border_style = 'outset'

table.add_row(["Name", "Age"])
table.add_row(["John Doe", 30])
table.add_row(["Jane Doe", 25])

print(table)
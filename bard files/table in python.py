import prettytable

# Create a PrettyTable object
table = prettytable.PrettyTable()

# Add rows and columns to the table
table.add_column('Name', ['John Doe', 'Jane Doe'])
table.add_column('Age', [30, 25])
table.add_column('Occupation', ['Software Engineer', 'Teacher'])

# Get the string representation of the table
table_string = str(table)

# Print the table
print(table_string)
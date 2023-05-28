from tabulate import tabulate

def print_table(data):
    print(tabulate(data, tablefmt='fancy_grid', showindex='always'))  

def print_table_with_headers(data):
    print(tabulate(data, headers='keys', tablefmt='fancy_grid', showindex='always'))

if __name__ == "__main__":
    # print_table_with_headers([
    print_table([
        ['Name', 'Age', 'Gender'],
        ['John', 20, 'Male'],
        ['Mary', 25, 'Female'],
        ['Peter', 30, 'Male'],
        ['Anna', 35, 'Female'],
        ['Michael', 40, 'Male']
    ])
    

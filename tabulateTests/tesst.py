from tabulate import tabulate


def print_table(data):
    print(tabulate(data, headers='keys', tablefmt='fancy_grid', showindex='always'))


def print_table_with_headers(data):
    print(tabulate(data, headers='keys', tablefmt='fancy_grid', showindex='never'))
    # print_table(data, headers='keys', tablefmt='fancy_grid', showindex='always')


if __name__ == "__main__":
    print_table_with_headers([
        ['Name', 'Age', 'Gender'],
        ['John', 20, 'Male'],
        ['Mary', 25, 'Female'],
        ['Peter', 30, 'Male'],
        ['Anna', 35, 'Female'],
        ['Janet', 40, 'Male'],
        ['Julia', 50, 'Female'],
        ['Jan', 60, 'Female']
    ])

import tabulate

from tabulate import tabulate


def print_table(data):
    print(tabulate(data, headers='keys', tablefmt='fancy_grid', showindex='always'))


def print_table_with_headers(data):
    print(tabulate(data, headers='keys', tablefmt='fancy_grid', showindex='alwaya'))
    # print_table(data, headers='keys', tablefmt='fancy_grid', showindex='always')


if __name__ == "__main__":
    print_table_with_headers([
        ['Subject', 'Backlog'],
        ['Math Manual', 'Completion'],
        ['Science Manual', 'Completion'],
        ['Social', 'Civics Chapter 4 Notes Completion']
    ])

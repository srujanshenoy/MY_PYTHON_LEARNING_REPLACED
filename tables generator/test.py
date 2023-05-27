from tabulate import tabulate

data = [["name", "age", "height", "weight", "Job"],
        ["John", 30, 1.75, "65kg", "Engineer"],
        ["Jane", 25, 1.75, "65kg", "Doctor"],
        ["Mary", 25, 1.75, "65kg", "Engineer"],
        ["Peter", 30, 1.75, "65kg", "Programmer"]
        ]

print(tabulate(data, headers="firstrow", showindex='always', tablefmt="fancy_grid"))
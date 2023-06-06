from tabulate import tabulate

formulae = {
    "Derived Physical Quantities": ["Area", "Volume", "Density", "Speed", "Velocity",
                                    "Acceleration", "Force", "Work", "Energy", "Power", "Pressure"],

    "Formulae": ["Area = l * b", "Volume = l * b * h", "Density = mass / volume = m / v",
                 "Speed = m / s",
                 "Velocity = displacement / time", "Acceleration = change of velocity / time",
                 "Force = Mass * Acceleration", "Work = Force * displacement",
                 "Energy = Work Done", "Power = Work Done / Time", "Pressure = Force / Area"],

    "Units": ["m^2", "m^3", "kg/m^3", "m/s", "m/s", "m/s^2", "kgm/s^2 or newtons (N)s",
              "kgm^2/s^2 or Joules(J)", "kgm^2/s^2 or Joules(J)", "kgm^2/s^3 or watts (W)",
              "n/m^2 or pascals (Pa)"]
}

# COEFFICIENTS OF MULTIPLICATION

multiplictaion_data = {
    "Multiplication Factor": [10, "10^2 (or) 100", "10^3 (or) 1000", "10^6 (or) 1000000",
                              "10^(-1) (or) 1/10", "10^(-2) (or) 1/100", "10^(-3) (or) 1/1000"],
    "Prefix": ["Deca", "Hecto", "kilo", "mega", "deci", "centi", "milli"],
    "Symbol": ["da", "h", "k", "M", "d", "c", "m"]
}

formulae_table = tabulate(formulae, headers="keys", tablefmt='fancy_grid', showindex=True)

# FUNDAMENTAL PHYSICAL QUANTITIES

fundamentals_data = {
    "quantities": [""],
    "units": [""]
}

if __name__ == "__main__":
    print("DERIVED PHYSICAL QUANTITIES:")
    print(formulae_table)

    print("MULTIPLES AND SUB-MULTIPLES")
    print(tabulate(multiplictaion_data, headers="keys", showindex=True, tablefmt="fancy_grid"))

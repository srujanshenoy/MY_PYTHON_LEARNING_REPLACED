import random

# Generate 100 random float values between 0 and 1
random_floats = [random.random() for _ in range(100)]

with open("CSV.csv", "wt") as file:
    file.write(str(random_floats))

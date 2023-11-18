with open("CSV.csv", "rt") as myfile:
    contents = myfile.read()

# Split the string by commas and store in a list
values_list = contents.split(',')

float_val_list = [] 
for element in values_list: float_val_list.append(float(element))

# Print the list of values
print(f"{float_val_list} \nmaximium: {max(float_val_list)}\nminimum: {min(float_val_list)}")


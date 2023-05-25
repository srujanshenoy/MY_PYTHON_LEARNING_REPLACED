def get_numbers_with_bit_set(numbers, bit_position):
    result = []
    for num in numbers:
        if num & (1 << bit_position):
            result.append(num)
    return result

# Define the numbers from 1 to 63
numbers = list(range(1, 64))
""" enter for the second number for which power you are generating the palette """

# Define the bit positions (1, 2, 4, 8, 16, 32)
bit_positions = [0, 1, 2, 3, 4]
""" Add how many places in binary your numbers go up to."""

# Categorize the numbers based on the bit positions
categories = {}
for bit_position in bit_positions:
    category = get_numbers_with_bit_set(numbers, bit_position)
    categories[2 ** bit_position] = category

# Print the categories
for category, numbers in categories.items():
    print(f"Category {category}: {numbers}")
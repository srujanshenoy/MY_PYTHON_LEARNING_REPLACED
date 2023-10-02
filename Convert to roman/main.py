# Function to convert decimal to Roman numerals
def decimal_to_roman(decimal):
    roman_numerals = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }

    result = ''
    for value in sorted(roman_numerals.keys(), reverse=True):
        while decimal >= value:
            result += roman_numerals[value]
            decimal -= value

    return result


# Function to convert Roman numerals to decimal
def roman_to_decimal(roman):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    decimal = 0
    prev_value = 0
    for numeral in reversed(roman):
        value = roman_numerals[numeral]
        if value < prev_value:
            decimal -= value
        else:
            decimal += value
        prev_value = value

    return decimal


# Main program
while True:
    print("Choose an option:")
    print("1. Decimal to Roman")
    print("2. Roman to Decimal")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        decimal_input = int(input("Enter a decimal number: "))
        if 1 <= decimal_input <= 3999:
            roman_output = decimal_to_roman(decimal_input)
            print(f"Roman numeral: {roman_output}")
        else:
            print("Please enter a valid decimal number (1-3999).")

    elif choice == '2':
        roman_input = input("Enter a Roman numeral: ")
        if all(numeral in 'IVXLCDM' for numeral in roman_input):
            decimal_output = roman_to_decimal(roman_input)
            print(f"Decimal number: {decimal_output}")
        else:
            print("Please enter a valid Roman numeral.")

    elif choice == '3':
        break

    else:
        print("Invalid choice. Please select a valid option.")

def print_number(count, number, OUT_STR):
    match count:
        case 1:
            OUT_STR += (numbers_mapping.get(number, "NAN") + " ")
        case 2:
            OUT_STR += 'double ' + (numbers_mapping.get(number, "NAN") + " ")
        case 3:
            OUT_STR += 'triple ' + (numbers_mapping.get(number, "NAN") + " ")
    return OUT_STR

phone = input("Phone number: ")
numbers_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero",
}

OUT_STR = ""
prev_number = 'x'
count = 1
for number in phone:
    if prev_number == number and count < 3:
        count += 1
    elif prev_number == number and count == 3:
        OUT_STR = print_number(count, prev_number, OUT_STR)
        count = 1
    elif prev_number == 'x':
        prev_number = number
        count = 1
    else:
        OUT_STR = print_number(count, prev_number, OUT_STR)
        prev_number = number
        count = 1
OUT_STR = print_number(count, prev_number, OUT_STR)
print(OUT_STR)

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

for number in phone:
    OUT_STR += (numbers_mapping.get(number, "NAN") + " ")

print(OUT_STR)

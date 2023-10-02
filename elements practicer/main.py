from elements_dict import elements

current_element = 0

while True:
    current_element += 1

    input()
    if current_element <= len(elements): print(elements[current_element])
    else: break

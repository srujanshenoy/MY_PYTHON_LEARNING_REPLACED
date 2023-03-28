def list_entrance_function():
    print("type anything and then hit space and then enter 1 time to nd entering.")
    input_list = []
    current_index = -1
    while True:
        input_list.append(input(">>>"))
        current_index += 1
        # if input_list[current_index - 1] == ' ' and input_list[current_index] == ' ':
        #     break
        # else:
        #     continue

        if input_list[current_index] == ' ':
            break
        else:
            continue

    input_list.pop(current_index)
    return input_list


def sum_list(in_list: list):
    current_index = 0
    for element in in_list:
        if current_index > 0:
            current_sum = previous_sum + element
            current_index += 1
            previous_sum = current_sum
        else:
            previous_sum = 0
            current_sum = element
            current_index += 1

    return current_sum + in_list[0]


def floating_list(inlist: list):
    current_index = 0
    outlist = []
    current_number = 0
    for char in inlist:
        try:
            current_number = float(char)
        except:
            continue

        outlist.append(current_number)

    return outlist

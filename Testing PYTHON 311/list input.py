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


# My_list = list_entrance_function()

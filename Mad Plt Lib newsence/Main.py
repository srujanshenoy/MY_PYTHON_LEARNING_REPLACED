ALHPA = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("welcome to matt plot lib")
dict_of_prompts = {
    "blank_lvl": 3,
    1: "I bought a new __1__\nand a new __2__\nto make my __3__\nstupid"
}

def ask_mat_plot(dictionary_of_prompts:dict, number:int):
    blank_lvl_of_prompts = dictionary_of_prompts["blank_lvl"]
    joke = dictionary_of_prompts[number]

    filling = []

    for i in range(blank_lvl_of_prompts):


    for i in range(blank_lvl_of_prompts + 1):
        current_input = input(f"__{i}__ ")
        filling.append(current_input)


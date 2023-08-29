import random

Jokes = {
    0: "What do you call a dinosaur that can't see?\na do-you-think-he-saurus!",
    1: "why did the golfer get a spare pant? In case he got a hole in one!",
    2: "What did one hat say to another? You stay here, I'll go on a-head!",
    3: "What did the sharpener say to the pencil? You're looking sharp!",
    4: "I told the doctor I broke my arm in two places. He told me not to go into those places.",
    5: "Why was the calendar nervous? Its days were numbered.",
    6: "Do you know why giraffes have such long necks? Because their heads are way up there.",
    7: "How do you catch a runaway laptop? With an internet.",
    8: "Two goldfish are in a tank. One turns to the other and says, \"Do you know how to drive this thing?\"",
    9: "Why do seagulls fly over the sea? Because if they flew over the bay, they'd be bagels.",
    10: "What did the zero say to the eight? \"Nice belt.\"",
    11: "Why did the chicken cross the road, roll in the mud and cross the road again? Because he was a dirty double "
        "crosser.",
    12: "Do monsters eat popcorn with their fingers? No, they eat the fingers separately.",
    13: "To steal ideas from one person is plagiarism. To steal from many is research.",
    14: "Some people say the glass is half full. Some people say the glass is half empty. Engineers say the glass is "
        "twice as big as necessary.",
    15: "What do you do when you see a spaceman? Park in it, man!"
}

continue_joking_var = True


def give_joke(jokes_dict: dict):
    """
    :param jokes_dict: the jokes dictionary to select a joke
    :return: none
    """

    print(jokes_dict[random.randint(0, len(jokes_dict) - 1)])
    
    
def continue_joking():
    usr_in = input("Another one? (enter for yes, anything followed by enter for no): ")
    if usr_in == '':
        return True
        
    return False


# Main loop
while continue_joking_var:
    give_joke(Jokes)
    continue_joking_var = continue_joking()
    
print("""You've been trolled, Have a nice day!""")

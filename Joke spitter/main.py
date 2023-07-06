import random

Jokes = {
    0: "What do you call a dinosaur that can't see?\na do-you-think-he-saurus!",
    1: "why did the golfer get a spare pant? In case he got a hole in one!",
    2: "What did one hat say to another? You stay here, I'll go on a-head!",
    3: "What did the sharpener say to the pencil? You're looking sharp!",
    4: "I told the doctor I broke my arm in two places. He told me not to go into those places.",
    5: "Why was the calendar nervous? Its days were numbered.",
    6: "Do you know why giraffes have such long necks? Because their heads are way up there.",
    7: "Helvetica walks into a bar. Bartender says, \"We don't want your type here!\" Where is Helvetica welcome? "
       "Say, \"Open Word.\"",
    8: "How do you catch a runaway laptop? With an internet.",
    9: "Two goldfish are in a tank. One turns to the other and says, \"Do you know how to drive this thing?\"",
    10: "Why do seagulls fly over the sea? Because if they flew over the bay, they'd be bagels.",
    11: "What did the zero say to the eight? \"Nice belt.\"",
    12: "Why did the chicken cross the road, roll in the mud and cross the road again? Because he was a dirty double "
        "crosser.",
    13: "Do monsters eat popcorn with their fingers? No, they eat the fingers separately.",
    14: "To steal ideas from one person is plagiarism. To steal from many is research.",
    15: "Some people say the glass is half full. Some people say the glass is half empty. Engineers say the glass is "
        "twice as big as necessary.",
    16: "I stayed up all night trying to see where the SUN went, and then it dawned on me. Got an idea dawning on "
        "you? Say, \"Open OneNote\" to jot, it down.",
    17: "What do you do when you see a spaceman? Park in it, man!",
    18: ("William Shakespeare owned a pencil that he chewed on so much, we don’t know if it’s 2B or not 2B. Want to \n"
         "protect your pencils? Say, “Start an email.”")
    19: 'Why did the hipster burn his mouth on his coffee? Because he drank it before it was cool.'
    20: 'A ham sandwich walks into a bar and the bartender says, "Sorry, we don\'t serve food in here."'
}


def give_joke(jokes_dict: dict):
    """
    :param jokes_dict: the jokes dictionary to select a joke
    :return: none
    """
    joke_in_dict = random.randint(0, len(jokes_dict) - 1)
    joke = jokes_dict[joke_in_dict]

    print(joke)


def another_one():
    """
    asks the user if they want to continue or not.
    :return: bool
    """
    print("do you want another one? if yes press enter, if not type anything and press enter")
    usr_in = input(">>> ")

    if usr_in == "":
        return True

    return False

global give_joke_var

give_joke_var = True

while give_joke_var:
    give_joke(Jokes)
    give_joke_var = another_one()



import random

Jokes = {
    0: "What do you call a dinosaur that can't see?\na do-you-think-he-saurus!",
    1: "why did the golfer get a spare pant? In case he got a hole in one!",
    2: "What did one hat say to another? You stay here, I'll go on a-head!",
    3: "What did the sharpener say to the pencil? You're looking sharp!",
    4: "I told the doctor I broke my arm in two places. He told me not to go into those places.",
    5: "Why was the calendar nervous? Its days were numbered."
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



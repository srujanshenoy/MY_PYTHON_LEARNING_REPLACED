import random

jokes = {
    1: "what do you call a fish w/o eyes?",
    'r1': "a fsh!"
    }

while True:
    random_no = random.randint(0, 1)
    input(f"{jokes[random_no]} (Press enter for response)")
    response_check = input(f"{jokes[f'r{random_no}']}")
    if response_check in (" ", ""):
        continue
    break

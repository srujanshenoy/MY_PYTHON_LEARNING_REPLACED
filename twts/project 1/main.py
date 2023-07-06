print("Welcome to my Computer Quiz!")

qa_dict = {
    1: ["What language does a computer use on the backend?", "Binary"]
}

def play_request():
    playing = 'False'

    while playing.lower() not in ['y', 'n']:
        playing = input("Do you want to Play? ")
        playing = playing.lower()

    if playing == 'y': playing = True
    if playing == 'n': playing = False

def check_answer(question_answer_dict:dict, question_number:int, user_answer:str):
    """
    :param question_answer_dict: The Dictionary that contains the questions and answers
    :param question_number: The question number to check
    :param user_answer: the answer given by the user
    :return: boolean, Correct / Incorrect answer
    """

    if user_answer.lower() != question_answer_dict[question_number[2]].lower(): return False
    else: return True

def ask_question(question_answer_dict:dict, question_number:int):
    usr_in = input(question_answer_dict[question_number[1]] + ' Answer: ')
    return usr_in

def play_question(question_answer_dict:dict, question_number:int):
    usr_answer = ask_question(question_answer_dict, question_number)
    check_answer(usr_answer)

while play_request():
    play_question(qa_dict, 1)



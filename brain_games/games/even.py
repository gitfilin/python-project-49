import random


def game_func():
    questions = 'Answer "yes" if the number is even, otherwise answer "no".'
    data = random.randint(1, 100)
    if data % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return data, right_answer, questions

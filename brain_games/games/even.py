import random


def game_func():
    questions = 'Answer "yes" if the number is even, otherwise answer "no".'
    result = random.randint(1, 100)
    if result % 2 == 0:
        answer_user = 'yes'
    else:
        answer_user = 'no'
    return result, answer_user, questions

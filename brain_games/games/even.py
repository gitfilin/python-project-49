import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round_data():
    data = random.randint(1, 100)
    if data % 2 == 0:
        answer_user = 'yes'
    else:
        answer_user = 'no'
    return data, answer_user

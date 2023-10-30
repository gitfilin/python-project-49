import random

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_even():
    result = random.randint(1, 100)
    if result % 2 == 0:
        answer_user = 'yes'
    else:
        answer_user = 'no'
    return result, answer_user

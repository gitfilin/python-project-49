import random


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime():
    k = 0
    result = random.randint(1, 100)
    for i in range(2, result // 2 + 1):
        if (result % i == 0):
            k = k + 1
    if (k <= 0):
        answer_user = 'yes'
    else:
        answer_user = 'no'
    return result, answer_user

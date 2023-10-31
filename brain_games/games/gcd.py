import random
import math


def game_func():
    questions = 'Find the greatest common divisor of given numbers.'
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    questions_nod = f'{a} {b}'
    result = math.gcd(a, b)
    answer_user = str(questions_nod)
    return result, answer_user, questions

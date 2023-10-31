import random
import math


def game_func():
    questions = 'Find the greatest common divisor of given numbers.'
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    data = f'{a} {b}'
    questions_nod = math.gcd(a, b)
    right_answer = str(questions_nod)
    return data, right_answer, questions

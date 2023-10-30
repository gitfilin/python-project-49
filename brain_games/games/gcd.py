import random
import math


QUESTION = 'Find the greatest common divisor of given numbers.'


def game_gcd():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    c = f'{a} {b}'
    result = math.gcd(a, b)
    answer_user = str(result)
    return c, answer_user

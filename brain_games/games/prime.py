import math
import random


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime():
    result = random.randint(1, 100)
    if result < 2:
        return result, 'no'
    for i in range(2, math.isqrt(result) + 1):
        if result % i == 0:
            return result, 'no'
    return result, 'yes'

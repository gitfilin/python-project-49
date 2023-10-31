import math
import random


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, math.isqrt(number) + 1):
        if number % i == 0:
            return False
    return True


def game_func():
    questions = 'Find the greatest common divisor of given numbers.'
    data = random.randint(1, 100)
    is_prime_result = is_prime(data)
    if is_prime_result:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return data, right_answer, questions

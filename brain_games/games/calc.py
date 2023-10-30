import random

QUESTION = 'What is the result of the expression?'


def game_calc():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])

    if operator == '+':
        result = str(a) + f' {operator} ' + str(b)
        answer = a + b

    elif operator == '-':
        result = str(a) + f' {operator} ' + str(b)
        answer = a - b
    else:
        result = str(a) + f' {operator} ' + str(b)
        answer = a * b

    return result, str(answer)

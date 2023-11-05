import random

DESCRIPTION = 'What is the result of the expression?'


def generate_round_data():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])

    if operator == '+':
        answer = a + b

    elif operator == '-':
        answer = a - b
    else:
        answer = a * b
    data = f'{a} {operator} {b}'
    right_answer = str(answer)

    return data, right_answer

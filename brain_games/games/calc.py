import random


def game_func():
    question = 'What is the result of the expression?'
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])

    if operator == '+':
        data = f'{a} {operator} {b}'
        answer = a + b

    elif operator == '-':
        data = f'{a} {operator} {b}'
        answer = a - b
    else:
        data = f'{a} {operator} {b}'
        answer = a * b
    right_answer = str(answer)

    return data, right_answer, question

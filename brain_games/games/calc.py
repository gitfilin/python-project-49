import random


def game_func():
    question = 'What is the result of the expression?'
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])

    if operator == '+':
        result = f'{a} {operator} {b}'
        answer = a + b

    elif operator == '-':
        result = f'{a} {operator} {b}'
        answer = a - b
    else:
        result = f'{a} {operator} {b}'
        answer = a * b
    answer_user = str(answer)

    return result, answer_user, question

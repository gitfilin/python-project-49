import random

DESCRIPTION = 'What number is missing in the progression?'


def generates_progression():
    start_sequence = random.randint(1, 100)
    step = random.randint(2, 10)
    row_length = random.randint(5, 10)
    progression = []

    for i in range(row_length):
        progression.append(start_sequence + i * step)
    return progression


def generate_round_data():
    generated_sequence = generates_progression()
    random_index = random.randint(0, len(generated_sequence) - 1)
    index = generated_sequence[random_index]

    generated_sequence[random_index] = '..'
    data = ' '.join([str(x) for x in generated_sequence])
    right_answer = str(index)

    return data, right_answer

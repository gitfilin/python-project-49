import random

QUESTION = 'What number is missing in the progression?'


def generates_progression():
    start_sequence = random.randint(1, 100)
    step = random.randint(2, 10)
    row_length = random.randint(5, 10)
    task = []

    for i in range(row_length):
        task.append(start_sequence + i * step)
    return task


def generates_example():
    generated_sequence = generates_progression()
    generated_number = random.randint(0, len(generated_sequence) - 1)
    result_list = generated_sequence[generated_number]

    generated_sequence[generated_number] = '..'
    data = ' '.join([str(x) for x in generated_sequence])
    right_answer = str(result_list)

    return data, right_answer

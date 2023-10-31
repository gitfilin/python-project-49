import random


def is_progression():
    start_sequence = random.randint(1, 100)
    step = random.randint(2, 10)
    row_length = random.randint(5, 10)
    new_list = []

    for i in range(row_length):
        new_list.append(start_sequence + i * step)
    return new_list


def game_func():
    questions = 'What number is missing in the progression?'
    new_list = is_progression()
    random_index = random.randint(0, len(new_list) - 1)
    result_list = new_list[random_index]

    new_list[random_index] = '..'
    result = ' '.join([str(x) for x in new_list])
    answer_user = str(result_list)

    return result, answer_user, questions

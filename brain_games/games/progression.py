import random


QUESTION = 'What number is missing in the progression?'


def game_progression():

    start_sequence = random.randint(1, 100)  # Введите первый номер члена a1:
    step = random.randint(2, 10)  # Введите разность ар.пр. :
    row_length = random.randint(5, 10)  # Введите последний номер члена k:

    new_list = []

    for i in range(row_length):
        new_list.append(start_sequence + i * step)

    random_index = random.randint(
        0, len(new_list) - 1)  # индекс случайного числа

    result = new_list[random_index]  # сохпаняем число кторое нужно угадать

    # print(result) #проверка числа

    new_list[random_index] = '..'  # скрываем число по индексу random_index
    result_list = ' '.join([str(x) for x in new_list])

    return result_list, str(result)

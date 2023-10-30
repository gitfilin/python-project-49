import prompt
from brain_games.cli import welcome_user


def game_engine(QUESTION, game_func):
    name = welcome_user()
    print(QUESTION)
    COUNT = 3
    while COUNT > 0:
        result, answer = game_func()
        print(f'Question {result}')
        an_user = prompt.string('Your answer: ')
        if answer == an_user:
            print('Correct!')
            COUNT -= 1
        else:
            print(
                f"'{an_user}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            break
        if COUNT == 0:
            print(f"Congratulations, {name}")
    return

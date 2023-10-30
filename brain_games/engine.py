import prompt
from brain_games.cli import welcome_user


def game_engine(question, game_func):
    name = welcome_user()
    print(question)
    for count in range(0, 3, 1):
        result, answer = game_func()
        print(f'Question: {result}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            quit()

    print(f"Congratulations, {name}!")

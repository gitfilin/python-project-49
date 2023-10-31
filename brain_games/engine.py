import prompt
from brain_games.cli import welcome_user


def game_engine(func):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(func.question)
    for _ in range(0, 3, 1):
        print(f'Question: {func.data}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == func.right_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{func.right_answer}'.")
            print(f"Let's try again, {name}!")
            break
        print(f"Congratulations, {name}!")

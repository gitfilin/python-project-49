import prompt


def game_engine(module):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(module.QUESTION)
    for _ in range(0, 3, 1):
        data, right_answer = module.generates_example()
        print(f'Question: {data}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == right_answer.right_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{right_answer.right_answer}'.")
            print(f"Let's try again, {name}!")
            break
        print(f"Congratulations, {name}!")

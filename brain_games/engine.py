import prompt

ROUNDS_COUNT = 3  # количество вопросов-ответов в игре
MAX_VALUE = 100  # максимальное значение для случайных чисел в играх


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES)
    for i in range(0, ROUNDS_COUNT):
        (question, answer) = game.get_question_and_answer()
        print(f"Question: {question}")
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'."
                  f"\nLet\'s try again, {name}!")
            exit()
    print(f'Congratulations, {name}!')

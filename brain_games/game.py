import prompt

ITERATIONS_NUMBER = 3  # количество вопросов-ответов в игре
MAX_VALUE = 100  # максимальное значение для случайных чисел в играх


def game(rules, question_and_answer):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(rules)
    for i in range(0, ITERATIONS_NUMBER):
        (question, answer) = question_and_answer()
        print(f"Question: {question}")
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{user_answer}'."
                  f"\nLet\'s try again, {name}!")
            exit()
    print(f'Congratulations, {name}!')

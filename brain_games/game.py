import prompt

ITERATIONS_NUMBER = 3  # количество вопросов-ответов в игре
MAX_VALUE = 100  # максимальное значение для случайных чисел в играх


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def check_answer(expected_answer, name):
    user_answer = prompt.string('Your answer: ')
    if user_answer == expected_answer:
        print('Correct!')
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{expected_answer}'."
              f"\nLet\'s try again, {name}!")
        return False


def game(rules, question_and_answer):
    name = welcome_user()
    print(rules)
    for i in range(0, ITERATIONS_NUMBER):
        (question, answer) = question_and_answer()
        print(f"Question: {question}")
        if not check_answer(answer, name):
            exit()
    print(f'Congratulations, {name}!')

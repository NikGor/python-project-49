import prompt

ITERATIONS_NUMBER = 3  # количество вопросов-ответов в игре
MAX_VALUE = 100  # максимальное значение для случайных чисел в играх
CALC_OPERATIONS_NUMBER = 2  # количество операций в игре калькулятор
CALC_MAX_VALUE = 10  # максимальное значение чисел для игры калькулятор


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
        print(f"{user_answer} is wrong answer ;(. "
              f"Correct answer was {expected_answer}."
              f"\nLet\'s try again, {name}!\n")
        return False


def main():
    welcome_user()


if __name__ == '__main__':
    main()

import random


CALC_OPERATIONS_NUMBER = 2  # количество операций в игре калькулятор
CALC_MAX_VALUE = 10  # максимальное значение чисел для игры калькулятор
RULES = 'What is the result of the expression?'


def get_question_and_answer():
    random1 = random.randint(0, CALC_MAX_VALUE)
    random2 = random.randint(0, CALC_MAX_VALUE)
    operation = random.randint(1, CALC_OPERATIONS_NUMBER)
    question_and_answer = ('', '')
    if operation == 1:
        question = f'{random1} + {random2}'
        answer = random1 + random2
        question_and_answer = (question, str(answer))
    elif operation == 2:
        question = f'{random1} * {random2}'
        answer = random1 * random2
        question_and_answer = (question, str(answer))
    return question_and_answer

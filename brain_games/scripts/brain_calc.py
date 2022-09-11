#!/usr/bin/env python3


import random
from brain_games.game import game
from brain_games.game import ITERATIONS_NUMBER
from brain_games.game import CALC_OPERATIONS_NUMBER
from brain_games.game import CALC_MAX_VALUE


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


def get_questions_and_answers():
    questions_and_answers = list()
    for i in range(0, ITERATIONS_NUMBER):
        questions_and_answers.append(get_question_and_answer())
    return questions_and_answers


def main():
    game(RULES, get_questions_and_answers())


if __name__ == '__main__':
    main()

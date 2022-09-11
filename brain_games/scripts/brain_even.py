#!/usr/bin/env python3


import random
from brain_games.game import game
from brain_games.game import ITERATIONS_NUMBER
from brain_games.game import MAX_VALUE


RULES = 'Answer "yes" if number even otherwise answer "no".'


def get_question_and_answer():
    rand = random.randint(0, MAX_VALUE)
    question_and_answer = (rand, is_even(rand) and 'yes' or 'no')
    return question_and_answer


def get_questions_and_answers():
    questions_and_answers = list()
    for i in range(0, ITERATIONS_NUMBER):
        questions_and_answers.append(get_question_and_answer())
    return questions_and_answers


def is_even(number):
    return number % 2 == 0


def main():
    game(RULES, get_questions_and_answers())


if __name__ == '__main__':
    main()

#!/usr/bin/env python3


import random
from brain_games.game import welcome_user
from brain_games.game import check_answer
from brain_games.game import ITERATIONS_NUMBER
from brain_games.game import MAX_VALUE


RULES = 'Answer "yes" if number even otherwise answer "no".'


def get_question_and_answer():
    rand = random.randint(0, MAX_VALUE)
    question_and_answer = (rand, is_even(rand) and 'yes' or 'no')
    return question_and_answer


def is_even(number):
    return number % 2 == 0


def main():
    name = welcome_user()
    print(RULES)
    for i in range(0, ITERATIONS_NUMBER):
        (question, answer) = get_question_and_answer()
        print(f"Question: {question}")
        if not check_answer(answer, name):
            exit()
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import random
from brain_games.game import welcome_user
from brain_games.game import check_answer
from brain_games.game import ITERATIONS_NUMBER
from brain_games.game import MAX_VALUE


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    rand = random.randint(0, MAX_VALUE)
    question_and_answer = (rand, is_prime(rand) and 'yes' or 'no')
    return question_and_answer


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number // 2):
        if number % i == 0:
            return False
    return True


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

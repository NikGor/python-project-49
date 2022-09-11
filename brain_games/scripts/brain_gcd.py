#!/usr/bin/env python3


import random
from brain_games.game import welcome_user
from brain_games.game import check_answer
from brain_games.game import ITERATIONS_NUMBER
from brain_games.game import MAX_VALUE


RULES = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    rand1 = random.randint(1, MAX_VALUE)
    rand2 = random.randint(1, MAX_VALUE)
    question_and_answer = (f'{rand1}, {rand2}', str(get_gcd(rand1, rand2)))
    return question_and_answer


def get_gcd(number1, number2):
    maximum = max(number1, number2)
    minimum = min(number1, number2)
    gcd = 1
    if maximum % minimum == 0:
        gcd = minimum
    else:
        cd = minimum
        while cd > 1:
            if minimum % cd == 0 and maximum % cd == 0:
                gcd = cd
            cd -= 1
    return gcd


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

#!/usr/bin/env python3

import prompt
import random

# from scripts.brain_even import RULES
# from scripts.brain_even import get_questions_and_answers

ITERATIONS_NUMBER = 3
RULES = 'Find the greatest common divisor of given numbers.'
MAX_VALUE = 100


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_questions_and_answers():
    questions_and_answers = list()
    for i in range(0, ITERATIONS_NUMBER):
        rand1 = random.randint(1, MAX_VALUE)
        rand2 = random.randint(1, MAX_VALUE)
        question_and_answer = (f'{rand1}, {rand2}', str(get_gcd(rand1, rand2)))
        questions_and_answers.append(question_and_answer)
    return questions_and_answers


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
    name = welcome_user()
    print(RULES)
    questions_and_answers = get_questions_and_answers()
    counter = 0
    for i in range(0, ITERATIONS_NUMBER):
        (question, answer) = questions_and_answers[i - 1]
        print(f"Question: {question}")
        if check_answer(answer, name):
            counter += 1
        else:
            break
    if counter == ITERATIONS_NUMBER:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()

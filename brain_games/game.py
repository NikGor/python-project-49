#!/usr/bin/env python3


import prompt

# from scripts.brain_even import RULES
# from scripts.brain_even import get_questions_and_answers

ITERATIONS_NUMBER = 3
RULES = 'Answer "yes" if number even otherwise answer "no".'
MAX_VALUE = 100


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
    print('')


if __name__ == '__main__':
    main()

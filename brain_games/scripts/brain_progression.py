#!/usr/bin/env python3

import prompt
import random

# from scripts.brain_even import RULES
# from scripts.brain_even import get_questions_and_answers

ITERATIONS_NUMBER = 3
RULES = 'What number is missing in the progression?'
MAX_VALUE = 100


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_questions_and_answers():
    questions_and_answers = list()
    min_progression_length = 5
    additional_progression_length = 6
    max_step_value = 10
    for i in range(0, ITERATIONS_NUMBER):
        array = get_progression(min_progression_length, additional_progression_length, max_step_value)
        hidden_index = random.randint(0, len(array) - 1)
        question = progression_to_string(array, hidden_index)
        answer = (array[hidden_index])
        question_and_answer = (question, str(answer))
        questions_and_answers.append(question_and_answer)
    return questions_and_answers


def get_progression(min_progression_length, additional_progression_length, max_step_value):
    length = min_progression_length + random.randint(0, additional_progression_length)
    array = list()
    array.append(random.randint(0, MAX_VALUE))
    step = random.randint(1, max_step_value)
    for i in range(1, length):
        array.append(array[i - 1] + step)
    return array


def progression_to_string(progression, hidden_index):
    string = ""
    for i in range(0, hidden_index):
        string += f'{progression[i]}, '
    string += '.., '
    for i in range(hidden_index + 1, len(progression)):
        string += f'{progression[i]}, '
    return string


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

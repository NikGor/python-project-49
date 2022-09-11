#!/usr/bin/env python3


import random
from brain_games.game import welcome_user
from brain_games.game import check_answer
from brain_games.game import ITERATIONS_NUMBER
from brain_games.game import MAX_VALUE


RULES = 'What number is missing in the progression?'


def get_question_and_answer():
    min_progression_length = 5
    additional_progression_length = 6
    max_step_value = 10
    array = get_progression(min_progression_length,
                            additional_progression_length,
                            max_step_value)
    hidden_index = random.randint(0, len(array) - 1)
    question = progression_to_string(array, hidden_index)
    answer = (array[hidden_index])
    question_and_answer = (question, str(answer))
    return question_and_answer


def get_progression(min_progression_length,
                    additional_progression_length,
                    max_step_value):
    length = min_progression_length + \
        random.randint(0, additional_progression_length)
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

#!/usr/bin/env python3


import random
from brain_games.game import game
from brain_games.game import ITERATIONS_NUMBER
from brain_games.game import MAX_VALUE
from brain_games.game import MIN_PROGRESSION_LENGTH
from brain_games.game import ADDITIONAL_PROGRESSION_LENGTH
from brain_games.game import MAX_STEP_VALUE


RULES = 'What number is missing in the progression?'


def get_question_and_answer():
    array = get_progression(MIN_PROGRESSION_LENGTH,
                            ADDITIONAL_PROGRESSION_LENGTH,
                            MAX_STEP_VALUE)
    hidden_index = random.randint(0, len(array) - 1)
    question = progression_to_string(array, hidden_index)
    answer = (array[hidden_index])
    question_and_answer = (question, str(answer))
    return question_and_answer


def get_questions_and_answers():
    questions_and_answers = list()
    for i in range(0, ITERATIONS_NUMBER):
        questions_and_answers.append(get_question_and_answer())
    return questions_and_answers


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
        string += f'{progression[i]} '
    string += '.. '
    for i in range(hidden_index + 1, len(progression)):
        string += f'{progression[i]} '
    return string


def main():
    game(RULES, get_questions_and_answers())


if __name__ == '__main__':
    main()

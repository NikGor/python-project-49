import random
from brain_games.game import MAX_VALUE


MIN_PROGRESSION_LENGTH = 5  # минимальная длина прогрессии
ADDITIONAL_PROGRESSION_LENGTH = 5  # плюс к длине прогрессии
MAX_STEP_VALUE = 10  # максимальный шаг прогрессии
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

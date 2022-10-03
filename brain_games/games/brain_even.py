import random
from brain_games.game import MAX_VALUE


RULES = 'Answer "yes" if number even, otherwise answer "no".'


def get_question_and_answer():
    rand = random.randint(0, MAX_VALUE)
    question_and_answer = (rand, is_even(rand) and 'yes' or 'no')
    return question_and_answer


def is_even(number):
    return number % 2 == 0

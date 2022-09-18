import random
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

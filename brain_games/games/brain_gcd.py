import random
from brain_games.game import MAX_VALUE


RULES = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    rand1 = random.randint(1, MAX_VALUE)
    rand2 = random.randint(1, MAX_VALUE)
    question_and_answer = (f'{rand1} {rand2}', str(get_gcd(rand1, rand2)))
    return question_and_answer


def get_gcd(number1, number2):
    maximum = max(number1, number2)
    gcd = 1
    for i in range(1, maximum + 1):
        if (number1 % i == 0) and (number2 % i == 0):
            gcd = i
    return gcd

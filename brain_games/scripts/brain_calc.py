#!/usr/bin/env python3


from brain_games.game import game
from brain_games.games.brain_calc import get_question_and_answer
from brain_games.games.brain_calc import RULES


def main():
    game(RULES, get_question_and_answer)


if __name__ == '__main__':
    main()

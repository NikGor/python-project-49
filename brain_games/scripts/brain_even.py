#!/usr/bin/env python3


from brain_games.game import game
from brain_games.games.brain_even import RULES
from brain_games.games.brain_even import get_question_and_answer


def main():
    game(RULES, get_question_and_answer)


if __name__ == '__main__':
    main()

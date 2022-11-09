#!/usr/bin/env python3

from brain_games.main import game
from brain_games.games.brain_progression import progression_game


RULE = 'What number is missing in the progression?'


def main():
    game(RULE, progression_game)


if __name__ == '__main__':
    main()

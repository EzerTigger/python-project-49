#!/usr/bin/env python3

from brain_games.main import game
from brain_games.games.brain_calc import calc_game, RULE


def main():
    game(RULE, calc_game)


if __name__ == '__main__':
    main()

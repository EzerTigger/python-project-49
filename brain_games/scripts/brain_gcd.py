#!/usr/bin/env python3

from brain_games.main import game
from brain_games.games.brain_gcd import gcd_game


RULE = 'Find the greatest common divisor of given numbers.'


def main():
    game(RULE, gcd_game)


if __name__ == '__main__':
    main()

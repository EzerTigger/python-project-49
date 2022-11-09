#!/usr/bin/env python3

from brain_games.main import game
from brain_games.games.brain_prime import prime_game

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    game(RULE, prime_game)


if __name__ == '__main__':
    main()

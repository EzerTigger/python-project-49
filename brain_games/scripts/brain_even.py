#!/usr/bin/env python3

from brain_games.main import game
from brain_games.games.brain_even import even_game, RULE


def main():
    game(RULE, even_game)


if __name__ == '__main__':
    main()

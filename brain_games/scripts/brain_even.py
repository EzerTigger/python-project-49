#!/usr/bin/env python3

from brain_games.main import game
from brain_games.games.brain_even import even_game


game_begin = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    game(game_begin, even_game)


if __name__ == '__main__':
    main()

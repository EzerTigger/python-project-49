#!/usr/bin/env python3

from brain_games.main import *
from brain_games.games.brain_calc import *

def main():
    welcome()
    calc()
    if rounds:
        lose()
    else:
        win()



if __name__ == '__main__':
    main()



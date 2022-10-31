#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.join(sys.path[0], '/home/user/hexlet-project1/brain_games/'))

from cli import welcome_user


def greet():
	print('Welcome to the Brain Games!')


def main():
	greet()
	welcome_user()

if __name__ == '__main__':
	main()


from random import randint
import prompt
from brain_games.main import *


def even():
    rounds = 3
    print('Welcome to the Brain Games!')
    username = get_username()
    welcome_user(username)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while rounds:
        question = randint(1, 100)
        get_question(question)
        answer = prompt.string('Your answer: ')
        if question % 2 == 0:
            result = 'yes'
        else:
            result = 'no'
        if answer == result:
            print('Correct!')
            rounds -= 1
        else:
            break
    if not rounds:
        win(username)
    else:
        lose(answer, result, username)
    

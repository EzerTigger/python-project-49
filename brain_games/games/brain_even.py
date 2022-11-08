from random import randint
import prompt
from brain_games.main import get_username, get_question, welcome_user, end


def even():
    ROUNDS = 3
    print('Welcome to the Brain Games!')
    username = get_username()
    welcome_user(username)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while ROUNDS:
        question = randint(1, 100)
        get_question(question)
        answer = prompt.string('Your answer: ')
        if question % 2 == 0:
            result = 'yes'
        else:
            result = 'no'
        if answer == result:
            print('Correct!')
            ROUNDS -= 1
        else:
            break
    end(ROUNDS, username, answer, result)

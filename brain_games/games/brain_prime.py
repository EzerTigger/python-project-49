from random import randint
import prompt
from brain_games.main import get_username, get_question, welcome_user, win, lose


def is_prime(x):
    divider = x // 2
    while divider > 1:
        if x % divider == 0:
            return 'no'
        else:
            divider -= 1
    return 'yes'


def prime():
    ROUNDS = 3
    print('Welcome to the Brain Games!')
    username = get_username()
    welcome_user(username)
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while ROUNDS:
        question = randint(1, 100)
        get_question(question)
        answer = prompt.string('Your answer: ')
        result = is_prime(question)
        if answer == result:
            print('Correct!')
            ROUNDS -= 1
        else:
            break
    if not ROUNDS:
        win(username)
    else:
        lose(answer, result, username)
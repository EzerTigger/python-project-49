from brain_games.main import get_username, get_question, welcome_user, end
from random import randint
import prompt


def find_gcd(a, b):
    gcd = min(a, b)
    while gcd > 0:
        if a % gcd == 0 and b % gcd == 0:
            return gcd
        else:
            gcd -= 1
    return gcd


def gcd():
    ROUNDS = 3
    print('Welcome to the Brain Games!')
    username = get_username()
    welcome_user(username)
    print('Find the greatest common divisor of given numbers.')
    while ROUNDS:
        a = randint(1, 100)
        b = randint(1, 100)
        question = f'{a} {b}'
        get_question(question)
        answer = prompt.string('Your answer: ')
        result = find_gcd(a, b)
        if answer == str(result):
            print('Correct!')
            ROUNDS -= 1
        else:
            break
    end(ROUNDS, username, answer, result)

from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


MIN_INTEGER = 1
MAX_INTEGER = 100


def get_game():
    number = randint(MIN_INTEGER, MAX_INTEGER)
    question = number
    if is_even(question):
        result = 'yes'
    else:
        result = 'no'
    return question, result

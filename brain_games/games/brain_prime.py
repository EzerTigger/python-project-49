from random import randint

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    divider = number // 2
    while divider > 1:
        if number % divider == 0:
            return False
        else:
            divider -= 1
    return True


MIN_INTEGER = 2
MAX_INTEGER = 100


def get_game():
    number = randint(MIN_INTEGER, MAX_INTEGER)
    question = number
    if is_prime(question):
        result = 'yes'
    else:
        result = 'no'
    return question, result

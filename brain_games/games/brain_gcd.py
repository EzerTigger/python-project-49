from random import randint

RULE = 'Find the greatest common divisor of given numbers.'


def find_gcd(first_number, second_number):
    gcd = min(first_number, second_number)
    while gcd > 0:
        if first_number % gcd == 0 and second_number % gcd == 0:
            return gcd
        else:
            gcd -= 1
    return gcd


MIN_INTEGER = 1
MAX_INTEGER = 100


def get_game():
    first_number = randint(MIN_INTEGER, MAX_INTEGER)
    second_number = randint(MIN_INTEGER, MAX_INTEGER)
    question = f'{first_number} {second_number}'
    result = find_gcd(first_number, second_number)
    return question, result

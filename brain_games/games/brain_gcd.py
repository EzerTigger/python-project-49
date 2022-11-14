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


def get_game():
    FIRST_NUMBER = randint(1, 100)
    SECOND_NUMBER = randint(1, 100)
    question = f'{FIRST_NUMBER} {SECOND_NUMBER}'
    result = find_gcd(FIRST_NUMBER, SECOND_NUMBER)
    return question, result

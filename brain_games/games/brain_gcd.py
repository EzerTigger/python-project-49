from random import randint

RULE = 'Find the greatest common divisor of given numbers.'


def find_gcd(a, b):
    gcd = min(a, b)
    while gcd > 0:
        if a % gcd == 0 and b % gcd == 0:
            return gcd
        else:
            gcd -= 1
    return gcd


def gcd_game():
    a = randint(1, 100)
    b = randint(1, 100)
    question = f'{a} {b}'
    result = find_gcd(a, b)
    return question, result

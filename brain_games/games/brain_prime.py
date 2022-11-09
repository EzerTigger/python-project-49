from random import randint


def is_prime(x):
    divider = x // 2
    while divider > 1:
        if x % divider == 0:
            return 'no'
        else:
            divider -= 1
    return 'yes'


def prime_game():
    question = randint(2, 100)
    result = is_prime(question)
    return question, result

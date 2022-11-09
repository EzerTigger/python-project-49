from random import randint


def is_prime(x):
    divider = x // 2
    while divider > 1:
        if x % divider == 0:
            return False
        else:
            divider -= 1
    return True


def prime_game():
    question = randint(2, 100)
    if is_prime(question):
        result = 'yes'
    else:
        result = 'no'
    return question, result

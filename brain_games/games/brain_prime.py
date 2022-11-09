from random import randint

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(x):
    divider = x // 2
    while divider > 1:
        if x % divider == 0:
            return False
        else:
            divider -= 1
    return True


def game():
    question = randint(2, 100)
    if is_prime(question):
        result = 'yes'
    else:
        result = 'no'
    return question, result

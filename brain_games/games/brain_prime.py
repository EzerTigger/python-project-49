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


def get_game():
    RANDOM_NUMBER = randint(2, 100)
    question = RANDOM_NUMBER
    if is_prime(question):
        result = 'yes'
    else:
        result = 'no'
    return question, result

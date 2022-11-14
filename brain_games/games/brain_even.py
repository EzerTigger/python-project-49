from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_game():
    RANDOM_NUMBER = randint(1, 100)
    question = RANDOM_NUMBER
    if is_even(question):
        result = 'yes'
    else:
        result = 'no'
    return question, result

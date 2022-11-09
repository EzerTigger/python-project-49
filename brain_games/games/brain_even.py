from random import randint


def is_even(x):
    return x % 2 == 0


def even_game():
    question = randint(1, 100)
    if is_even(question):
        result = 'yes'
    else:
        result = 'no'
    return question, result

from random import randint


def is_even(x):
    if x % 2 == 0:
        return 'yes'
    else:
        return 'no'


def even_question():
    question = randint(1, 100)
    return question


def even_game():
    question = even_question()
    result = is_even(question)
    return question, result

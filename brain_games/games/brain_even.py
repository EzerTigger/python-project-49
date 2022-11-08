from random import randint


def even_begin():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def even_question():
    question = randint(1, 100)
    return question


def even_result(question):
    if question % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result

from random import randint, choice


def get_expression(a, b, op):
    if op == ' + ':
        result = a + b
    elif op == ' - ':
        result = a - b
    elif op == ' * ':
        result = a * b
    return result


def calc_game():
    a = randint(1, 12)
    b = randint(1, 12)
    operator = choice([' + ', ' - ', ' * '])
    question = str(a) + operator + str(b)
    result = get_expression(a, b, operator)
    return question, result

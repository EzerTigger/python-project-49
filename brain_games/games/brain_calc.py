from random import randint, choice

RULE = 'What is the result of the expression?'


def get_expression(first_number, second_number, operator):
    if operator == ' + ':
        expression = first_number + second_number
    elif operator == ' - ':
        expression = first_number - second_number
    elif operator == ' * ':
        expression = first_number * second_number
    return expression


OPERATORS = [' + ', ' - ', ' * ']
MIN_INTEGER = 1
MAX_INTEGER = 12


def get_game():
    first_number = randint(MIN_INTEGER, MAX_INTEGER)
    second_number = randint(MIN_INTEGER, MAX_INTEGER)
    operator = choice(OPERATORS)
    question = str(first_number) + operator + str(second_number)
    result = get_expression(first_number, second_number, operator)
    return question, result

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


OPERATOR = choice([' + ', ' - ', ' * '])


def get_game():
    FIRST_NUMBER = randint(1, 12)
    SECOND_NUMBER = randint(1, 12)
    question = str(FIRST_NUMBER) + OPERATOR + str(SECOND_NUMBER)
    result = get_expression(FIRST_NUMBER, SECOND_NUMBER, OPERATOR)
    return question, result

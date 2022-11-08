import prompt
from random import randint, choice
from brain_games.main import get_username, get_question, welcome_user, end


def get_expression(a, b, op):
    if op == ' + ':
        result = a + b
    elif op == ' - ':
        result = a - b
    elif op == ' * ':
        result = a * b
    return result


def calc():
    ROUNDS = 3
    print('Welcome to the Brain Games!')
    username = get_username()
    welcome_user(username)
    print('What is the result of the expression?')
    while ROUNDS:
        a = randint(1, 12)
        b = randint(1, 12)
        operator = choice([' + ', ' - ', ' * '])
        question = str(a) + operator + str(b)
        get_question(question)
        result = get_expression(a, b, operator)
        answer = prompt.string('Your answer: ')
        if answer == str(result):
            print('Correct!')
            ROUNDS -= 1
        else:
            break
    end(ROUNDS, username, answer, result)

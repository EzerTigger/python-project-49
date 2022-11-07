import prompt
from random import randint, choice
from brain_games.main import get_username, get_question, welcome_user, win, lose


# Оно работает!)
def calc():
    rounds = 3
    print('Welcome to the Brain Games!')
    username = get_username()
    welcome_user(username)
    print('What is the result of the expression?')
    while rounds:
        a = randint(1, 12)
        b = randint(1, 12)
        operator = choice([' + ', ' - ', ' * '])
        question = str(a) + operator + str(b)
        get_question(question)
        if operator == ' + ':
            result = a + b
        elif operator == ' - ':
            result = a - b
        elif operator == ' * ':
            result = a * b
        answer = prompt.string('Your answer: ')
        if answer == str(result):
            print('Correct!')
            rounds -= 1
        else:
            break
    if not rounds:
        win(username)
    else:
        lose(answer, result, username)

import prompt
from random import randint, choice


def calc():
    rounds = 3
    print('What is the result of the expression?')
    while rounds:
        a = randint(1, 12)
        b = randint(1, 12)
        expression = choice([f'{a} + {b}', f'{a} - {b}', f'{a} * {b}'])
        print(f'Question: {expression}')
        results = {f'{a} + {b}': a + b, f'{a} - {b}': a - b, f'{a} * {b}': a * b}
        result = results[expression]
        answer = prompt.string('Your answer: ')
        if answer == str(result):
            print('Correct!')
            rounds -= 1
        else:
            break
    return rounds, answer, result


rounds, answer, result = calc()



















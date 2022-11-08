from brain_games.main import get_question, get_username, welcome_user, end
from random import randint
import prompt


def make_progression():
    first_el = randint(1, 20)
    prog = [first_el]
    step = randint(1, 10)
    while len(prog) < 10:
        prog.append(prog[-1] + step)
    return prog


def progression():
    ROUNDS = 3
    print('Welcome to the Brain Games!')
    username = get_username()
    welcome_user(username)
    print('What number is missing in the progression?')
    while ROUNDS:
        prog = make_progression()
        idx = randint(0, len(prog) - 1)
        question = " ".join(str(el) for el in prog).replace(str(prog[idx]),
                                                            '..', 1)
        get_question(question)
        answer = prompt.string('Your answer: ')
        result = str(prog[idx])
        if answer == str(result):
            print('Correct!')
            ROUNDS -= 1
        else:
            break
    end(ROUNDS, username, answer, result)

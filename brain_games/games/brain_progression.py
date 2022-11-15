from random import randint

RULE = 'What number is missing in the progression?'


def make_progression():
    first_el = randint(1, 20)
    prog = [first_el]
    step = randint(1, 10)
    while len(prog) < 10:
        prog.append(prog[-1] + step)
    return prog


def get_game():
    progression = make_progression()
    index_of_lost_char = randint(0, len(progression) - 1)
    question = " ".join(str(el) for el in progression).replace(
               str(progression[index_of_lost_char]), '..', 1)
    result = str(progression[index_of_lost_char])
    return question, result

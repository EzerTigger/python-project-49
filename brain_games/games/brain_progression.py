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
    INDEX_OF_LOST_CHAR = randint(0, len(progression) - 1)
    question = " ".join(str(el) for el in progression).replace(
               str(progression[INDEX_OF_LOST_CHAR]), '..', 1)
    result = str(progression[INDEX_OF_LOST_CHAR])
    return question, result

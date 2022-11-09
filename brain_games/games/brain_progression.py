from random import randint


def make_progression():
    first_el = randint(1, 20)
    prog = [first_el]
    step = randint(1, 10)
    while len(prog) < 10:
        prog.append(prog[-1] + step)
    return prog


def progression_game():
    prog = make_progression()
    idx = randint(0, len(prog) - 1)
    question = " ".join(str(el) for el in prog).replace(str(prog[idx]),
                                                        '..', 1)
    result = str(prog[idx])
    return question, result

import prompt


def get_username():
    name = prompt.string('May I have your name? ')
    return name


def welcome_user(name):
    print(f"Hello, {name}")


def get_answer():
    answer = prompt.string('Your answer: ')
    return answer


def get_question(question):
    print(f'Question: {question}')


def lose(ans, res, name):
    print(f"{ans} is wrong answer ;(. Correct answer was {res}."
          f" Let's try again, {name}!")


def win(name):
    print(f'Congratulations, {name}!')


def end(rounds, name, ans, res):
    if not rounds:
        win(name)
    else:
        lose(ans, res, name)


def game(game_begin, which_game):
    ROUNDS = 3
    print('Welcome to the Brain Games!')
    username = get_username()
    welcome_user(username)
    print(game_begin)
    while ROUNDS:
        question, result = which_game()
        get_question(question)
        answer = get_answer()
        if answer == str(result):
            print('Correct!')
            ROUNDS -= 1
        else:
            break
    end(ROUNDS, username, answer, result)

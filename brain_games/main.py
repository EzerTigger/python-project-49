import prompt
from brain_games.games.brain_even import even_begin, even_question, even_result


def get_username():
    name = prompt.string('May I have your name? ')
    return name


def welcome_user(name):
    print(f"hello, {name}")


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


def main_even():
    ROUNDS = 3
    print('Welcome to the Brain Games!')
    username = get_username()
    welcome_user(username)
    even_begin()
    while ROUNDS:
        question = even_question()
        get_question(question)
        answer = get_answer()
        result = even_result(question)
        if answer == result:
            print('Correct!')
            ROUNDS -= 1
        else:
            break
    end(ROUNDS, username, answer, result)

import prompt


def get_username():
    name = prompt.string('May I have your name? ')
    return name


def welcome_user(name):
    print(f'Hello, {name}!')


def get_question(question):
    print(f'Question: {question}')


def lose(ans, res, name):
    print(f"{ans} is wrong answer ;(. Correct answer was {res}."
          f" Let's try again, {name}!")


def win(name):
    print(f'Congratulations, {name}!')

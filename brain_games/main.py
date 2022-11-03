import prompt


name = ''


def welcome():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')


def lose():
    print(f"{answer} is wrong answer ;(. Correct answer was {result}. Let's try again, {name}")


def win():
    print(f'Congratulations, {name}!')
    




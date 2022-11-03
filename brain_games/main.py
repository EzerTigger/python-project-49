import prompt


def welcome():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


name = welcome()



def end():
    if rounds:
        print(f"{answer} is wrong answer ;(. Correct answer was {result}. Let's try again, {name}")
    else:
        print(f'Congratulations, {name}!')


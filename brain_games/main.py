import prompt


def game(which_game):
    ROUNDS = 3
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f"Hello, {username}")
    print(which_game.RULE)
    while ROUNDS:
        question, result = which_game.get_game()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == str(result):
            print('Correct!')
            ROUNDS -= 1
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {result}."
                  f" Let's try again, {username}!")
            break
    else:
        print(f'Congratulations, {username}!')

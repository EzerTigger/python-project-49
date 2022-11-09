import prompt


def game(game_begin, which_game):
    ROUNDS = 3
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f"Hello, {username}")
    print(game_begin)
    while ROUNDS:
        question, result = which_game()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == str(result):
            print('Correct!')
            ROUNDS -= 1
        else:
            break
    if not ROUNDS:
        print(f'Congratulations, {username}!')
    else:
        print(f"{answer} is wrong answer ;(. Correct answer was {result}."
              f" Let's try again, {username}!")

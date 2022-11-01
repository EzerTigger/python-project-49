from random import randint
import prompt


def even():
    rounds = 3

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ') 
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while rounds:
        question = randint(1, 100)
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if question % 2 == 0:
            if answer == 'yes':
                print('Correct!')
                rounds -= 1
            else:
                print(f"{answer} is wrong answer ;(. Correct answer was 'yes'. Let's try again, {name}")
                break
        if question % 2:
            if answer == 'no':
                print('Correct!')
                rounds -= 1
            else:
                print(f"{answer} is wrong answer ;(. Correct answer was 'no'. Let's try again, {name}")
                break
    if not rounds:        
        print(f'Congratulations, {name}!')


                




            

    
import prompt
import random


def createQuestionAnswer():
    number = random.randint(1, 100)
    return [number, 'yes'] if number % 2 == 0 else [number, 'no']


def even_game():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while (count < 3):
        count += 1
        question, result = createQuestionAnswer()
        print(f'Question: {question}')
        value = prompt.string('Your answer: ')
        if (value == result):
            print('Correct!')
        else:
            print(f'\'{value}\' is wrong answer ;(. Correct answer was \'{result}\'.')
            print('Let\'s try again, Bill!')
            return
    print(f'Congratulations, {name}!')

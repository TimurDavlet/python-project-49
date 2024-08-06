import prompt


def play_game(start_question, createQuestionAnswer):
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(start_question)
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
            print(f'Let\'s try again, {name}!')
            return
    print(f'Congratulations, {name}!')

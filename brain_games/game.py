import prompt


error_text = 'is wrong answer ;(. Correct answer was'


def play_game(start_question, createQuestionAnswer, max_round=3):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(start_question)
    count = 0
    while (count < max_round):
        count += 1
        question, result = createQuestionAnswer()
        print(f'Question: {question}')
        value = prompt.string('Your answer: ')
        if (value == result):
            print('Correct!')
        else:
            print(f'\'{value}\' {error_text} \'{result}\'.')
            print(f'Let\'s try again, {name}!')
            return
    print(f'Congratulations, {name}!')

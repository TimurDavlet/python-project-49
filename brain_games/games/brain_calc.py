from brain_games.game import play_game
from brain_games.random_number_generator import random_integer
from functools import partial


start_question = 'What is the result of the expression?'


def createQuestionAnswer():
    number1 = random_integer()
    number2 = random_integer()
    operations = ['+', '-', '*']
    random_operation = random_integer(0, 2)
    simbol = operations[random_operation]
    question_string = f'{str(number1)} {simbol} {str(number2)}'
    if (random_operation == 0):
        result_question = number1 + number2
    elif (random_operation == 1):
        result_question = number1 - number2
    else:
        result_question = number1 * number2
    return [question_string, str(result_question)]


play_game = partial(play_game, start_question, createQuestionAnswer)

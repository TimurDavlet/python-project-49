from brain_games.game import play_game
from brain_games.random_number_generator import random_integer
from functools import partial


start_question = 'Find the greatest common divisor of given numbers.'


def createQuestionAnswer():
    number1 = random_integer()
    number2 = random_integer()
    question_string = f'{number1} {number2}'
    result = number1 if number1 >= number2 else number2
    while (result != 1):
        if (number1 % result == 0 and number2 % result == 0):
            return [question_string, str(result)]
        result -= 1
    return [question_string, str(result)]


play_game = partial(play_game, start_question, createQuestionAnswer)

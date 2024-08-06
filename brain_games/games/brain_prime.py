from brain_games.game import play_game
from brain_games.random_number_generator import random_integer
from functools import partial


start_question = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def createQuestionAnswer():
    number = random_integer()
    result = 'no'
    for i in range(2, number):
        if (number % i == 0):
            return [str(number), result]
    return [str(number), 'yes']


play_game = partial(play_game, start_question, createQuestionAnswer)

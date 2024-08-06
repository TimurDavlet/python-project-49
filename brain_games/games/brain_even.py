from brain_games.game import play_game
from brain_games.random_number_generator import random_integer
from functools import partial


start_question = 'Answer "yes" if the number is even, otherwise answer "no".'


def createQuestionAnswer():
    number = random_integer()
    return [number, 'yes'] if number % 2 == 0 else [number, 'no']


play_game = partial(play_game, start_question, createQuestionAnswer)

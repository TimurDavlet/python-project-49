from brain_games.game import play_game
from brain_games.random_number_generator import random_integer
from functools import partial


start_question = 'What number is missing in the progression?'


def createQuestionAnswer():
    progression_list = []
    list_length = 9
    start_number = random_integer()
    step = random_integer(1, 10)
    hidden_index = random_integer(0, 9)
    result = 0
    while len(progression_list) <= list_length:
        if (len(progression_list) == hidden_index):
            result = start_number
            progression_list.append('..')
        else:
            progression_list.append(str(start_number))
        start_number += step
    return [' '.join(map(str, progression_list)), str(result)]


play_game = partial(play_game, start_question, createQuestionAnswer)

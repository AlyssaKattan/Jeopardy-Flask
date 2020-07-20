import random

def calc_points(game_info, answer):
    value = game_info['value']
    if value != "":
        if answer.lower() == game_info['answer'].lower():
            return value
        else:
            return value * -1

def calc_points(clue, answer):
    correct_answer= clue['answer'].lower()
    answer= answer.lower()
    if answer == correct_answer:
        return clue['value']
    else: 
        return (clue['value'])*-1
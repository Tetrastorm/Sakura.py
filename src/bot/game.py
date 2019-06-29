#
# Valentin Diard, 2019
#
# Project:     Sakura.py
# License:     MIT License
#
# File:        game.py
# Description: Manage games.
#

game_going_on = []

class game(object):
    __slots__ = ['channel_id', 'game_name', 'board', 'player_function']

    def __init__(self, channel_id, game_name, board, player_function):
        self.channel_id = channel_id
        self.game_name = game_name
        self.board = board
        self.player_function = player_function

def game_is_going_on_here(message):
    i = 0
    for current in game_going_on:
        if message.channel.id == current.channel_id:
            return i
        i += 1
    return -1
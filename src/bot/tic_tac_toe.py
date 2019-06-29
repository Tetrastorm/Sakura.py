#
# Valentin Diard, 2019
#
# Project:     Sakura.py
# License:     MIT License
#
# File:        tic_tac_toe.py
# Description: Code of the Tic Tac Toe game.
#

import random

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

def remove_current_game(current_game):
    global game_going_on
    tmp_list = []

    for game in game_going_on:
        if current_game.channel_id != game.channel_id:
            tmp_list += game
    game_going_on = tmp_list


async def game_manager(message):
    index = game_is_going_on_here(message)

    if -1 != index:
        await game_going_on[index].player_function(message)
        return True
    return False

def diplay_board(current_game):
    msg = ''

    for line in current_game.board:
        for cell in line:
            if cell == 0:
                msg += ':white_square_button:'
            elif cell == 1:
                msg += ':x:'
            else:
                msg += ':o:'
        msg += '\n'
    return msg

def check_victory(board, player):
    combinations = [
        # horizontal
        ((0,0), (1,0), (2,0)),
        ((0,1), (1,1), (2,1)),
        ((0,2), (1,2), (2,2)),
        # vertical
        ((0,0), (0,1), (0,2)),
        ((1,0), (1,1), (1,2)),
        ((2,0), (2,1), (2,2)),
        # crossed
        ((0,0), (1,1), (2,2)),
        ((2,0), (1,1), (0,2))
    ]
    tmp = 0

    for coordinates in combinations:
        for coord in coordinates:
            if board[coord[0]][coord[1]] != player:
                break
            tmp += 1
        if tmp == 3:
            return True
        tmp = 0
    return False

def have_no_space_available(board):
    space_available = 0

    for line in board:
        for cell in line:
            if cell == 0:
                space_available += 1
    if space_available == 0:
        return True
    return False

async def tic_tac_toe_game(message):
    global game_going_on
    game_exist = game_is_going_on_here(message)

    if game_exist == -1:
        game_going_on += [game(message.channel.id, 'tic-tac-toe', [[0,0,0], [0,0,0], [0,0,0]], player_turn)]
        await message.channel.send(diplay_board(game_going_on[game_is_going_on_here(message)]))
    else:
        await message.channel.send('**Error:** Tic Tac Toe game is currently going on.')

async def ai_turn(message):
    x = random.randint(0, 2)
    y = random.randint(0, 2)

    while game_going_on[game_is_going_on_here(message)].board[y][x] != 0:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
    game_going_on[game_is_going_on_here(message)].board[y][x] = -1
    await message.channel.send('It\'s my turn ^^')
    await message.channel.send('*Sakura.py played: ' + str(x + 1) + ' ' + str(y + 1) + '*')
    await message.channel.send(diplay_board(game_going_on[game_is_going_on_here(message)]))

async def player_turn(message):
    parse_msg = message.content.split(" ")
    x = int(parse_msg[0]) - 1
    y = int(parse_msg[1]) - 1

    if x < 3 and x >= 0 and y < 3 and y >= 0 and game_going_on[game_is_going_on_here(message)].board[y][x] == 0:
        await message.channel.send('*Player played: ' + message.content + '*')
        game_going_on[game_is_going_on_here(message)].board[y][x] = 1
        await message.channel.send(diplay_board(game_going_on[game_is_going_on_here(message)]))
    else:
        await message.channel.send('**Error:** Invalid request.')
        return

    if check_victory(game_going_on[game_is_going_on_here(message)].board, 1):
        await message.channel.send('Dammit! You win!!!')
        remove_current_game(game_going_on[game_is_going_on_here(message)])
        return

    if have_no_space_available(game_going_on[game_is_going_on_here(message)].board):
        await message.channel.send('We are stuck, GG!!!')
        remove_current_game(game_going_on[game_is_going_on_here(message)])
        return

    await ai_turn(message)

    if check_victory(game_going_on[game_is_going_on_here(message)].board, -1):
        await message.channel.send('Youpee! You lose!!!')
        remove_current_game(game_going_on[game_is_going_on_here(message)])
        return



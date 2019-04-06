import time
import random
from bot import bot

bot.in_game = ""
tic_tac_toe_map = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

async def tic_tac_toe_display(msg):
    message = ''
    for line in tic_tac_toe_map:
        for cell in line:
            if int(cell) == 0:
                message += ':white_square_button:'
            elif int(cell) == 1:
                message += ':x:'
            else:
                message += ':o:'
        message += '\n'
    await msg.channel.send(message)

def have_win():
    player = 0
    bot = 0
    for i in range(3):
        if tic_tac_toe_map[i][i] == 1:
            player += 1
        elif tic_tac_toe_map[i][i] == 2:
            bot += 1
    if bot == 3:
        return 2
    elif player == 3:
        return 1
    bot = 0
    player = 0
    for i in range(2, -1, -1):
        if tic_tac_toe_map[i - 2][i] == 1:
            player += 1
        elif tic_tac_toe_map[i - 2][i] == 2:
            bot += 1
    if bot == 3:
            return 2
    elif bot == 3:
        return 1
    for line in tic_tac_toe_map:
        if line == [1, 1, 1]:
            return 1
        elif line == [2, 2, 2]:
            return 2
    cell_empty = 0
    for line in tic_tac_toe_map:
        for cell in line:
            if cell == 0:
                cell_empty += 1
    if cell_empty == 0:
        return -1
    return 0

async def tic_tac_toe_game(message):
    global tic_tac_toe_map
    parse_msg = message.content.split(" ")

    if (int(parse_msg[0]) < 3 and int(parse_msg[0]) >= 0
        and int(parse_msg[1]) < 3 and int(parse_msg[1]) >= 0
        and tic_tac_toe_map[int(parse_msg[1])][int(parse_msg[0])] == 0):
        tic_tac_toe_map[int(parse_msg[1])][int(parse_msg[0])] = 1
        await tic_tac_toe_display(message)

        win_value = have_win()
        if win_value == 1:
            await message.channel.send('Dammit! You win!!!')
            tic_tac_toe_map = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            bot.in_game = ""
            return
        elif win_value == -1:
            await message.channel.send('We are stuck, GG!!!')
            tic_tac_toe_map = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            bot.in_game = ""
            return
        await message.channel.send('It\'s my turn ^^')
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        while tic_tac_toe_map[y][x] != 0:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
        tic_tac_toe_map[y][x] = 2
        await tic_tac_toe_display(message)
        if (have_win() == 2):
            await message.channel.send('Youpee! You lose!!!')
            tic_tac_toe_map = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            bot.in_game = ""
    else:
        await message.channel.send('Invalid input, please retry')

async def list_and_display_chan(message):
    chans = bot.get_all_channels()
    for chan in chans:
        print(chan.name)
        await message.channel.send('{0.name}'.format(chan))

@bot.event
async def on_member_join(member):
    guild = member.guild
    time.sleep(0.5)
    if guild.system_channel is not None:
        to_send = 'Welcome {0.mention}! (＾◡＾)'.format(member)
        await guild.system_channel.send(to_send)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('I heard you! {0.name}'.format(message.author))
    elif message.content.startswith('!help'):
        await message.channel.send('Commands:\n- !help\n- !hello\n')
    elif message.content.startswith('!list'):
        list_and_display_chan(message)
    elif message.content.startswith('!tic_tac_toe'):
        await message.channel.send('Enter: "x y" for indicate where you will place your pawn')
        bot.in_game = "tic_tac_toe"
    elif bot.in_game == "tic_tac_toe":
        await tic_tac_toe_game(message)

@bot.event
async def on_ready():
    print('------')
    print('Logged in as: {0.name}'.format(bot.user))
    print('Associate ID: {0.id}'.format(bot.user))
    print('------')
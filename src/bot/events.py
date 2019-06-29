#
# Valentin Diard, 2019
#
# Project:     Sakura.py
# License:     MIT License
#
# File:        events.py
# Description: Define all event used by the bot.
#

import time
from bot import bot
from config import cmdinputs, cmdactions
from bot import tic_tac_toe as tictac

@bot.event
async def on_member_join(member):
    guild = member.guild
    time.sleep(0.5)
    if guild.system_channel is not None:
        await guild.system_channel.send('Welcome {0.mention}! (＾◡＾)'.format(member))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    for x in range(0, len(cmdinputs)):
        if message.content == cmdinputs[x]:
            await cmdactions[x](message)
            return
    await tictac.game_manager(message)

@bot.event
async def on_ready():
    print('------')
    print('Logged in as: {0.name}'.format(bot.user))
    print('Associate ID: {0.id}'.format(bot.user))
    print('------')
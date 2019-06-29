#
# Valentin Diard, 2019
#
# Project:     Sakura.py
# License:     MIT License
#
# File:        commands.py
# Description: Define command behaviour.
#

from config import GITHUB_LINK

async def hello_cmd(message):
    await message.channel.send('I heard you! {0.name}'.format(message.author))

async def help_cmd(message):
    await message.channel.send('```Commands:\n- !help\n- !hello\n\nGame:\n- !tic_tac_toe\n\nOther:\n- !github```')

async def github_cmd(message):
    await message.channel.send('To follow the project, report an issue or contributing => ' + GITHUB_LINK)
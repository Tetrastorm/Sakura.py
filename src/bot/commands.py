#
# Valentin Diard, 2019
#
# Project:     Sakura.py
# License:     MIT License
#
# File:        commands.py
# Description: Define command behaviour.
#

from config import GITHUB_MSG, LINK_MSG, HELP_MSG, REALEASE_NOTE

async def hello_cmd(message):
    await message.channel.send('I heard you! {0.name}'.format(message.author))

async def help_cmd(message):
    msg = ''
    for line in HELP_MSG:
        msg += line
    await message.channel.send(msg)

async def release_cmd(message):
    msg = ''
    for line in REALEASE_NOTE:
        msg += line
    await message.channel.send(msg)

async def link_cmd(message):
    await message.channel.send(LINK_MSG)

async def github_cmd(message):
    await message.channel.send(GITHUB_MSG)
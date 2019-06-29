#
# Valentin Diard, 2019
#
# Project:     Sakura.py
# License:     MIT License
#
# File:        commands.py
# Description: Define command behaviour.
#

async def hello_cmd(message):
    await message.channel.send('I heard you! {0.name}'.format(message.author))

async def help_cmd(message):
    await message.channel.send('```Commands:\n- !help\n- !hello\n```')
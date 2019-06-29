#
# Valentin Diard, 2019
#
# Project:     Sakura.py
# License:     MIT License
#
# File:        __init__.py
# Description: init bot.
#

import discord
from config import TOKEN

bot = discord.Client()

from bot import events
from bot import tic_tac_toe as tictac
from bot import game


bot.run(TOKEN)
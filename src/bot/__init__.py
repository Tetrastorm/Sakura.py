import discord
from config import TOKEN

bot = discord.Client()

from bot import events

bot.run(TOKEN)
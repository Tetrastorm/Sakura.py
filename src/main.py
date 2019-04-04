#!/usr/bin/env python3
import discord

TOKEN = 'NTYyOTU5MTE5ODc1NzAyNzk1.XKXBrg.YluBZBb5t-O4eTygY7qVXYXa9gw'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('I heard you! {0.name}'.format(message.author))
    elif message.content.startswith('!help'):
        await message.channel.send('Commands:\n- !help\n- !hello\n')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)

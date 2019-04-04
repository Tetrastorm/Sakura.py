#!/usr/bin/env python3
import discord
import time

TOKEN = 'NTYyOTU5MTE5ODc1NzAyNzk1.XKXBrg.YluBZBb5t-O4eTygY7qVXYXa9gw'

client = discord.Client()

async def list_and_display_chan(message):
    chans = client.get_all_channels()
    for chan in chans:
        print(chan.name)
        await message.channel.send('{0.name}'.format(chan))

@client.event
async def on_member_join(member):
    guild = member.guild
    time.sleep(0.5)
    if guild.system_channel is not None:
        to_send = 'Welcome {0.mention}! (＾◡＾)'.format(member)
        await guild.system_channel.send(to_send)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('I heard you! {0.name}'.format(message.author))
    elif message.content.startswith('!help'):
        await message.channel.send('Commands:\n- !help\n- !hello\n')
    elif message.content.startswith('!list'):
        list_and_display_chan(message)

@client.event
async def on_ready():
    print('Logged in as: {0.name}'.format(client.user))
    print('Associete ID: {0.id}'.format(client.user))
    print('------')

client.run(TOKEN)

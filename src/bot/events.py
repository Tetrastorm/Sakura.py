import time
from bot import bot

def list_and_display_chan(message):
    chans = bot.get_all_channels()
    for chan in chans:
        print(chan.name)
        return message.channel.send('{0.name}'.format(chan))

def hello_cmd(message):
    return message.channel.send('I heard you! {0.name}'.format(message.author))

def help_cmd(message):
    return message.channel.send('Commands:\n- !help\n- !hello\n')

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
        await hello_cmd(message)
    elif message.content.startswith('!help'):
        awiat help_cmd(message)
    elif message.content.startswith('!list'):
        await list_and_display_chan(message)

@bot.event
async def on_ready():
    print('------')
    print('Logged in as: {0.name}'.format(bot.user))
    print('Associate ID: {0.id}'.format(bot.user))
    print('------')
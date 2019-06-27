def list_and_display_chan(message):
    chans = bot.get_all_channels()
    for chan in chans:
        print(chan.name)
        return message.channel.send('{0.name}'.format(chan))

def hello_cmd(message):
    return message.channel.send('I heard you! {0.name}'.format(message.author))

def help_cmd(message):
    return message.channel.send('Commands:\n- !help\n- !hello\n')
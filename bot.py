import discord
import logging
import pandas as pd

logging.basicConfig(level=logging.INFO)

client = discord.Client()
guild = discord.Guild

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('_'):

        cmd = message.content.split()[0].replace("_","")
        if len(message.content.split()) > 1:
            parameters = message.content.split()[1:]

        # Bot Commands

        if cmd == 'scan':
            data = pd.DataFrame(columns = ['content', 'time', 'author'])

        # history is a channel property, so we'll need the channel as an argument
        # if the command user does not inform the channel, use the message.channel atribute

    

client.run('NjAxNTM0NDgyOTczMDY1MjM4.XTDspA.o8F_hfWn2lkfAGYN-m9KeZ1czFs')
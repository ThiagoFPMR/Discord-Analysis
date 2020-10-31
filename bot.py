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

            data = pd.DataFrame(columns=['content', 'time', 'author'])

            # Acquiring the channel via the bot command
            if len(message.channel_mentions) > 0:
                channel = message.channel_mentions[0]
            else:
                channel = message.channel

            # Aquiring the number of messages to be scraped via the bot command
            if (len(message.content.split()) > 1 and len(message.channel_mentions) == 0) or len(message.content.split()) > 2:
                for parameter in parameters:
                    if parameter[0] != "<": # Channels are enveloped by "<>" as strings
                        limit = int(parameter)
            else:
                limit = 100

            print(limit)
            
            count = 0;
            async for msg in channel.history(limit=limit):
                if msg.author != client.user:
                    data = data.append({'content': msg.content,
                                        'time': msg.created_at,
                                        'author': msg.author.name}, ignore_index=True)
                    print(f"Added row {count} to dataframe")
                    count += 1
            
            data.to_csv('data/msg_hist.csv')

    

client.run('NjAxNTM0NDgyOTczMDY1MjM4.XTDspA.o8F_hfWn2lkfAGYN-m9KeZ1czFs')
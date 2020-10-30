import discord
import logging
import pandas as pd
import numpy as np

logging.basicConfig(level=logging.INFO)

client = discord.Client()
#guild. discord.Guild

@client.event
async def on_ready():
    guild = client.get_guild(532982579733856286)

    print('We have logged in as {0.user}'.format(client))
    async for message in guild.text_channels[0].history():
        print(message.content)

    

client.run('NjAxNTM0NDgyOTczMDY1MjM4.XlrJkA.xoJ1VTbC4GkM8-lUE0kd832k6v0')
import discord
import random


TOKEN = 'OTgyNTAzNzg5OTM0Mjk3MDg4.GAgsL1.rBjNNPwXvEgOL0ylo8WFc33kDU4qE3BxdA201A'

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is ready')

client.run(TOKEN)



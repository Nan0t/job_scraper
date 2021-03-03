import discord
import importlib
from src_scraper import buscarEmpleos
from tokens import *

client = discord.Client()

listaJobs=buscarEmpleos(["trainee","junior", "jr"])
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel=client.get_channel(jobs_channel_ID)
    for job in listaJobs:
        print(job)
        await channel.send(job)




client.run(tokenBOT)
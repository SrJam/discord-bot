import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!w2g')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Hello There') )
    print('Bot is ready.')

client.run('NzcyNTAxMzYyNjgzNTQzNTYz.X57l9Q.tiBFZwKM02qDv7emjtLBkNVxvFk')
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!w2g')

@client.event 
async def on_ready():
    print("bot is ready")

@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {round{client.latence * 1000}}')


client.run('NzcyNTAxMzYyNjgzNTQzNTYz.X57l9Q.tiBFZwKM02qDv7emjtLBkNVxvFk')
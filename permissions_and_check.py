import discord
from discord.ext import commands
import os


client = commands.Bot(command_prefix='!w2g')

@client.event
async def on_ready():
    print('Bot is ready.')


def is_it_me(ctx):
    return ctx.author.id == ###meu id

@client.command()
@commands.has_permissions(menage_messages=True)
@commands.check(is_it_me)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)



client.run('NzcyNTAxMzYyNjgzNTQzNTYz.X57l9Q.tiBFZwKM02qDv7emjtLBkNVxvFk')
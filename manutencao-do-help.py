import discord
import json
import os
from discord.ext import commands

client = commands.Bot(command_prefix= '!w2g')
client.remove_command('help')


@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping():
    await client.say('Pong!')

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='help')
    embed.add_field(name='ping', value='Returns pong!', inline=False)

    await client.send_message(author, embed=embed)


client.run('NzcyNTAxMzYyNjgzNTQzNTYz.X57l9Q.tiBFZwKM02qDv7emjtLBkNVxvFk')
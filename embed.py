import discord
import json
import os
from discord.ext import commands

client = commands.Bot(command_prefix= '!w2g')


@client.event
async def on_ready():
    print('Bot is ready.')

@client.command(pass_context=True)
async def displayembed(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(
        title =  'Title',
        description = 'This is a description',
        colour = discord.Colour.blue()
    )


    embed.set_footer(text='This is a footer')
    embed.set_image(url='')
    embed.set_thumbnail(url='')
    embed.set_author(name='Author Name', icon_url='')
    embed.add_field(name='Field Name', value='Field Value', inline=False)
    embed.add_field(name='Field Name', value='Field Value', inline=False)
    embed.add_field(name='Field Name', value='Field Value', inline=False)

    # await client.say(embed=embed)
    await client.send_message(channel, embed=embed)

client.run('NzcyNTAxMzYyNjgzNTQzNTYz.X57l9Q.tiBFZwKM02qDv7emjtLBkNVxvFk')
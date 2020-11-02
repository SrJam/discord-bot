import discord
import json
from discord.ext import commands

def get_prefix(client, message):
    with open('prefix.json', 'r') as f:
        prefixes = json.load(f)
    
    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix= get_prefix)

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_guild_join(guild):
    with open('prefix.json', 'r') as f:
        prefixes = json.load(f)
    
    prefixes[str(guild.id)] = '!w2g '

    with open('prefix.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefix.json', 'r') as f:
        prefixes = json.load(f)
    
    prefixes.pop(str(guild.id))

    with open('prefix.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.command()
async def changeprefix(ctx, prefix):
    with open('prefix.json', 'r') as f:
        prefixes = json.load(f)
    
    prefixes[str(ctx.id)] = prefix

    with open('prefix.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Prefix changed to: {prefix}')
    

client.run('NzcyNTAxMzYyNjgzNTQzNTYz.X57l9Q.tiBFZwKM02qDv7emjtLBkNVxvFk')
import discord
from discord.ext import commands
import os


client = commands.Bot(command_prefix='!w2g')
status = cycle(['Status 1', 'Status 2'])
@client.event
async def on_ready():
    print('Bot is ready.')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Passe todo os argumentos necessarios')


@clear.error #Error pra esse especifico comando, precisa do comando importado no script
async def clear_error(ctx, clear_error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Passe todo os argumentos necessarios')



client.run('NzcyNTAxMzYyNjgzNTQzNTYz.X57l9Q.tiBFZwKM02qDv7emjtLBkNVxvFk')
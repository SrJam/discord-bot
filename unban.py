import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!w2g')

@client.event 
async def on_ready():
    print("bot is ready")

@client.commands()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.namme, user.discriminator) ==  (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return


client.run('NzcyNTAxMzYyNjgzNTQzNTYz.X57l9Q.tiBFZwKM02qDv7emjtLBkNVxvFk')
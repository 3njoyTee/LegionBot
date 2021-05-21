import discord
import time
import subprocess
import sys
import os
import random
import asyncio
from time import sleep
from discord.ext import commands


filename = '/Users/3njoytee/Desktop/Bots/LegionBot/settings.txt'
with open(filename) as f:
    content = f.readlines()
settings = [x.strip() for x in content] 
UI = int(settings[1].split(' ', 2)[2], 16)
logs = settings[2].split(' ', 2)[2]
logs = int(logs)
icon = settings[3].split(' ', 2)[2]
icon = str(icon)
icn = icon
prefix = str(settings[4].split(' ', 2)[2])
token = str(settings[0].split(' ', 2)[2])
name = str(settings[5].split(' ', 2)[2])
guild_id = int(settings[6].split(' ', 2)[2])
command_emoji = str(settings[7].split(' ', 2)[2])

intents = discord.Intents.all()
client = commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command('help')


cross =  "❌"
check = "✔️ "


@client.event
async def on_command_error(ctx, error):
    Args = discord.Embed(
        description = cross + ' Please specify all arguments', colour = UI
    )
    Args.set_footer(text='For more help, do: ' + prefix + 'command [command]')
    Perms = discord.Embed(
        description = cross + " Looks like you don't have permission to do this", colour = UI
    )
    dm = discord.Embed(
        description = cross + ' This command cannot be run in DMs', colour = UI
    )
    notfound = discord.Embed(
        description = cross + ' This command does not exist', colour = UI
    )
    notfound.set_footer(text='For more help, do: ' + prefix + 'command [command]')
    membernotfound = discord.Embed(
        description = cross + ' This member does not exist', colour = UI
    )
    userrnotfound = discord.Embed(
        description = cross + ' This user does not exist', colour = UI
    )
    emojirnotfound = discord.Embed(
        description = cross + ' This emoji does not exist', colour = UI
    )
    botperms = discord.Embed(
        description = cross + " Looks like I don't have permission to do this", colour = UI
    )
    botperms.set_footer(text='Make sure you give me full permissions')
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=Args)
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed=Perms)
    if isinstance(error, commands.NoPrivateMessage):
        await ctx.send(embed=dm)
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(embed=notfound)
    if isinstance(error, commands.MemberNotFound):
        await ctx.send(embed=membernotfound)
    if isinstance(error, commands.UserNotFound):
        await ctx.send(embed=userrnotfound)
    if isinstance(error, commands.EmojiNotFound):
        await ctx.send(embed=emojirnotfound)
    if isinstance(error, commands.EmojiNotFound):
        await ctx.send(embed=emojirnotfound)
    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send(embed=botperms)
    if isinstance(error, commands.CommandInvokeError):
        print(error)
        error = error.original
        print(error)
    


    # BotMissingPermissions

@client.command()
async def status(ctx):
    await ctx.send(check + ' Bot is functioning')

@client.command()
async def ip(ctx):
    embed = discord.Embed(
        description = 'The server IP is: LegionMc.club', colour = UI
    )
    await ctx.send(embed=embed)


startup_extensions = [
    'cogs.help',
    'cogs.info',
    'cogs.moderation.purge',
    'cogs.moderation.ban',
    'cogs.moderation.kick',
    'cogs.moderation.unmute'
] 

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

@client.command()
async def coglist(ctx):
    if ctx.author.id == 511239599213772805:

        listing = '\n'.join(startup_extensions)

        embed=discord.Embed(
            title = 'Listing all cogs:',
            description = listing, 
            colour = UI
        )
        embed.set_footer(text=str(len(startup_extensions)) + ' cogs available')
        await ctx.send(embed=embed)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=prefix + "help"))
    print('Connected to bot: {}'.format(client.user.name))

client.run(token)


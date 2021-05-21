import discord
import time
import subprocess
import sys
import os
import random
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
guild_id = str(settings[6].split(' ', 2)[2])
command_emoji = str(settings[7].split(' ', 2)[2])

cross =  "❌"
check = "✔️ "

defined = 0
class ban(commands.Cog):
    print('ban cog loaded!')
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context = True)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason):
        nein = discord.Embed(
            description = cross + ' **You cannot ban yourself!**', colour = UI
        )
        embed = discord.Embed(
            description= tick + ' ' + member.display_name + " was banned successfully by " + ctx.author.name + " for: " + reason, color=UI
        )
        if member == None or member == ctx.message.author:
            await ctx.send(embed=nein)
            return
        if reason == None:
            reason = "No Reason Specified"
        await member.ban(reason=reason, delete_message_days=7)
        await ctx.send(embed=embed)
        embed.add_field(name='Ban', value='Action was done by' + ctx.author.mention, inline=True)
        await self.client.get_channel(logs).send(embed=embed)
        
       


def setup(client):
    client.add_cog(ban(client))

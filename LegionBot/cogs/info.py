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

class info(commands.Cog):
    print('info cog loaded!')
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def info(self, ctx, member:discord.Member):
        discon = ctx.guild.get_member(member.id).avatar_url
        joindate = ctx.guild.get_member(member.id).joined_at.strftime('%m/%d/%Y, %H:%M:%S')
        createdate = ctx.guild.get_member(member.id).created_at.strftime('%m/%d/%Y, %H:%M:%S')
        embed=discord.Embed(colour = UI)
        embed.set_author( name='Displaying background information of: ' + str(member), icon_url=discon)
        embed.set_thumbnail(url=discon)
        embed.add_field(name="Joined this server on:", value=joindate, inline=True)
        embed.add_field(name="Created on:", value=createdate, inline=True)
        embed.set_footer(text="User ID: " + str(member.id))
        
        await ctx.send(embed=embed)
        
def setup(client):
    client.add_cog(info(client))

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
guild_id = str(settings[6].split(' ', 2)[2])
command_emoji = str(settings[7].split(' ', 2)[2])

cross =  "❌"
check = "✔️ "

enabled = 'true'

class purge(commands.Cog):
    print('purge cog loaded!')
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages = True)
    async def purge(self, ctx, limit: int):
        await ctx.channel.purge(limit=limit)

        embed = discord.Embed(
            description=str(limit) + ' Messages purged by {}'.format(ctx.author.mention + ' in ' + ctx.channel.name), color=UI
        )
        await ctx.send(embed=embed)
        await self.client.get_channel(logs).send(embed=embed)


def setup(client):
    client.add_cog(purge(client))
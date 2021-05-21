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

class unmute(commands.Cog):
    print('unmute cog loaded!')
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context = True)
    #@commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member):
        embed = discord.Embed(
            description= check + " " + str(member.display_name) + " was unmuted successfully by " + ctx.author.mention, color=UI
        )
        await ctx.message.delete()
        
        mute_role = discord.utils.get(ctx.message.guild.roles, name='Muted')
        await member.remove_roles(mute_role)
        await member.send('You have been unmuted from ' + ctx.guild.name)
        # await ctx.send("Successfully Muted user for: " + reason)
        
        await ctx.send(embed=embed)
        embed.add_field(name='Unmute', value='Action was done by ' + ctx.author.mention, inline=True)
        await self.client.get_channel(logs).send(embed=embed)

    @commands.command(pass_context = True)
    async def serverinvite(self, ctx):
        await ctx.message.delete()
        terry = await ctx.channel.create_invite()
        await ctx.author.send(terry)
        
def setup(client):
    client.add_cog(unmute(client))

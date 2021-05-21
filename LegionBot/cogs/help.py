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


class help(commands.Cog):
    print('help cog loaded!')
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        
        embed=discord.Embed(title="Commands", color=UI)
        embed.set_author(name="Legion Bot", icon_url="https://cdn.discordapp.com/icons/747889056750370906/a86b286b42d90755186dccc5da11ca4b.png?size=4096")
        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/747889056750370906/a86b286b42d90755186dccc5da11ca4b.png?size=4096")
        embed.add_field(name="`Moderator`", value="`!moderator`", inline=True)
        embed.set_footer(text="https://discord.gg/legionmc")
        await ctx.send(embed=embed)
        

    @commands.command()
    async def moderator(self, ctx):
        embed=discord.Embed(title="Moderation", color=0x10242d)
        embed.set_author(name="Legion Bot", icon_url="https://cdn.discordapp.com/icons/747889056750370906/a86b286b42d90755186dccc5da11ca4b.png?size=4096")
        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/747889056750370906/a86b286b42d90755186dccc5da11ca4b.png?size=4096")
        embed.add_field(name="!kick ", value="Kick a user", inline=True)
        embed.add_field(name="!ban", value="Ban a user", inline=True)
        embed.add_field(name="!info ", value="View info of a user", inline=True)
        embed.add_field(name="!purge", value="Remove spam walls", inline=True)
        embed.add_field(name="!mute", value="Mute a user", inline=True) # Permanently tho
        embed.add_field(name="!unmute", value="Unmute a user", inline=True) # Permanently tho
        embed.set_footer(text="Moderation Commands")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(help(client))

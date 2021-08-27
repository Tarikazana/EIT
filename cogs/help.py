"""
> help.py
> Author: Tari Kazana
> does the helping thing

"""

from datetime import datetime
import json
import discord
from discord.ext import commands


class help(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command(name = "help")
    @commands.guild_only()
    @commands.has_permissions()
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def commandName(self, ctx:commands.Context):
        with open('eit/config.json', 'r') as config:
            conf = json.load(config)
            pref = conf["prefix"]
        embed=discord.Embed(title="Help", description=f"Commands:", color=0x00F3FF)
        embed.set_author(name=self.bot.user.name, icon_url=str(self.bot.user.avatar_url))

        embed.add_field(name=f"{pref}channel", value="set the log channel", inline=False)
        embed.timestamp = datetime.now()
        embed.set_footer(text="EIT | Developed by Tari#7072")
        await ctx.send(embed=embed)


def setup(bot:commands.Bot):
    bot.add_cog(help(bot))
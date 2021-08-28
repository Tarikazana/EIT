"""
> Channel.py
> Author: Tari Kazana
> setting log channel

"""

import discord
import json
from discord.ext import commands
from datetime import datetime


class Channel(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
    
    @commands.command(name = "channel", aliases=["setchannel"])
    @commands.guild_only()
    @commands.has_permissions(administrator = True)
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def  commandName(self, ctx:commands.Context,channel:discord.TextChannel):
        guild = ctx.message.guild

        idDict = "{"+f'"log-channel":"{channel.id}"'+"}"

        jsonString = json.dumps(idDict)
        jsonString = jsonString.replace('\\"','"')[1:-1]
        jsonFile = open(f"eit/server_configs/{guild.id}_config.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()

        await ctx.reply(f"Changed log channel to {channel.mention}")


def setup(bot:commands.Bot):
    bot.add_cog(Channel(bot))

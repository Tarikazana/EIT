"""
> OnJoin.py
> Author: Tari Kazana
> sending instructions

"""

import discord
import json
import os
from discord.ext import commands
from datetime import datetime


class OnJoin(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(self, member:discord.Member):
        guild = member.guild
        if os.path.isfile(f"eit/server_configs/{guild.id}_config.json"):
            with open(f'eit/server_configs/{guild.id}_config.json', 'r') as config:
                conf = json.load(config)
                log_channel_id = conf["log-channel"]
            logs = self.bot.get_channel(int(log_channel_id))
        else:
            logs = guild.system_channel

        embed=discord.Embed(title=" ", description="➥ joined the server", color=0x00F3FF)
        embed.set_author(name=str(member), icon_url=member.avatar_url)
        embed.set_footer(text="ID: " + str(member.id))
        embed.timestamp = member.joined_at

        with open(f"eit/data/active_invs_{guild.id}.json", 'r') as f:
            invfile = json.load(f)
        
        active_invs = await guild.invites()
        for inv in active_invs:
            check_inv = str(invfile[str(inv.code)]).split("---")

            if str(inv.uses) != str(check_inv[4]):
                embed.add_field(name="\u200b", value=f"Inviter: {check_inv[0]} (`{check_inv[1]}`)\nChannel: `{check_inv[2]}`\n\nCode: `{str(inv.code)}` | Uses: ` {str(int(check_inv[4])+1)} `\nCreated at: `{check_inv[5]}`\n\n*This server now has {guild.member_count} members*", inline=False)

        

        await logs.send(embed=embed)

        inv = ""
        
        for x in active_invs:
            inv = inv + f'"{str(x.code)}":"{str(x.inviter)}---{str(x.inviter.id)}---{str(x.channel)}---{str(x.url)}---{str(x.uses)}---{str(datetime.fromtimestamp(round(datetime.timestamp(x.created_at))))}",'
        inv = inv[:-1].replace("'","")
        
        idDict = "{"+f"{inv}"+"}"

        jsonString = json.dumps(idDict)
        jsonString = jsonString.replace('\\"','"')[1:-1]
        jsonFile = open(f"eit/data/active_invs_{guild.id}.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()


def setup(bot:commands.Bot):
    bot.add_cog(OnJoin(bot))
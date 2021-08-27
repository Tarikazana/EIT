"""
> OnInvite.py
> Author: Tari Kazana
> Invite updates

"""

import json
import discord
import os
from discord.ext import commands
from datetime import datetime


class OnInvite(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_invite_create(self, invite:discord.Invite):
        guild = invite.guild
        if os.path.isfile(f"eit/server_configs/{guild.id}_config.json"):
            with open(f'eit/server_configs/{guild.id}_config.json', 'r') as config:
                conf = json.load(config)
                log_channel_id = conf["log-channel"]
            logs = self.bot.get_channel(int(log_channel_id))
        else:
            logs = guild.system_channel


        time = invite.max_age
            
        if time == 0:
            time = "never"
        elif time > 86400:
            time = "7d"
        elif time > 43200:
            time = "1d"
        elif time > 21600:
            time = "12h"
        elif time > 3600:
            time = "6h"
        elif time > 1800:
            time = "1h"
        else: time = "30min"

        max_uses = invite.max_uses
        if max_uses == 0:
            max_uses = "∞"
            
        embed=discord.Embed(title=" ", description="➥ created invite", color=0x00F3FF)
        embed.set_author(name=str(invite.inviter), icon_url=invite.inviter.avatar_url)
        embed.add_field(name="Invite:", value=f"```code: {invite.code}\nchannel: {invite.channel}\nexpires after: {time}\nmax uses: {max_uses}\ntemporary: {str(invite.temporary).lower()}```", inline=False)
        embed.set_footer(text="ID: " + str(invite.inviter.id))
        embed.timestamp = datetime.now()
        await logs.send(embed=embed)

        active_invs = await guild.invites()
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
    bot.add_cog(OnInvite(bot))

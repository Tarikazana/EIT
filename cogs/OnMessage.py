"""
> OnMessage.py
> Author: Tari Kazana
> logs

"""

import discord
import json
import os
from discord.ext import commands
from datetime import datetime

class bcolors:
    CYAN = '\033[95m'       #PURPLE IN TERMINAL
    CYAN2 = '\033[94m'      #OKBLUE IN TERMINAL
    CYAN3 = '\033[96m'      #OKCYAN IN TERMINAL
    PURPLE = '\033[92m'     #OKGREEN IN TERMINAL
    PURPLE2 = '\033[91m'    #FAIL IN TERMINAL
    WARNING = '\033[93m'    #YELLOW IN TERMINAL
    ENDC = '\033[0m'        #same
    BOLD = '\033[1m'        #same
    UNDERLINE = '\033[4m'   #same


class OnMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        with open('eit/config.json', 'r') as config:
            conf = json.load(config)
        
        # current date and time
        now = datetime.now()
        timestamp = round(datetime.timestamp(now))

        if isinstance(message.channel, discord.channel.DMChannel):
            info = await self.bot.application_info()
            Tari = info.owner
            await message.author.send(f"Sorry, this bot is not accepting any DM's.\nFor questions ask {Tari}.")
        else:
            print(f"[{datetime.fromtimestamp(timestamp)}] {bcolors.CYAN3}{message.author} in {message.channel.name}{bcolors.ENDC}: {message.content}")


def setup(bot):
    bot.add_cog(OnMessage(bot))
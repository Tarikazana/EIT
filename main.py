"""
> main.py
> Author: Tari Kazana
> loading extensions

"""

import discord
import os
import json
import time

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

start = time.time()
print(f"{bcolors.CYAN}> init{bcolors.ENDC}")
class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

print(f"{bcolors.CYAN}> loading prefix{bcolors.ENDC}")
with open('eit/config.json', 'r') as config:
    conf = json.load(config)
    pref = conf["prefix"]
    token = conf["token"]
    version = conf["version"]

print(f"{bcolors.CYAN}> loading Intents{bcolors.ENDC}")
intents = discord.Intents.all()
bot = commands.Bot(pref, intents = intents, case_insensitive=True)

bot.remove_command('help')

print(f"{bcolors.CYAN}> loading cogs{bcolors.ENDC}")
if __name__ == '__main__':
    for filename in os.listdir("eit/cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"{bcolors.CYAN}>> {filename[:-3]} loaded.{bcolors.ENDC}")


@bot.event
async def on_ready():
    print(f"{bcolors.CYAN}> ready{bcolors.ENDC}\n")
    print(f"{bcolors.CYAN}██   ██   ███████ ██ ████████     ██████  ███████  █████  ██████  ██    ██ {bcolors.ENDC}")
    print(f"{bcolors.CYAN} ██   ██  ██      ██    ██        ██   ██ ██      ██   ██ ██   ██  ██  ██  {bcolors.ENDC}")
    print(f"{bcolors.CYAN}  ██   ██ █████   ██    ██        ██████  █████   ███████ ██   ██   ████   {bcolors.ENDC}")
    print(f"{bcolors.CYAN} ██   ██  ██      ██    ██        ██   ██ ██      ██   ██ ██   ██    ██    {bcolors.ENDC}")
    print(f"{bcolors.CYAN}██   ██   ███████ ██    ██        ██   ██ ███████ ██   ██ ██████     ██    {bcolors.ENDC}")

    # current date and time
    now = datetime.now()
    timestamp = round(datetime.timestamp(now))
    print(f"\n{bcolors.PURPLE}{datetime.fromtimestamp(timestamp)} - {bot.user} has connected to Discord!{bcolors.ENDC}")

    print ("------------------------------------")
    print (f"Bot Name: {bot.user.name}")
    print (f"Bot ID: {bot.user.id}")
    print (f"Bot Created: {datetime.fromtimestamp(round(datetime.timestamp(bot.user.created_at)))}")
    print (f"Discord Version: {discord.__version__}")
    print (f"Bot Version: {version}")
    print ("------------------------------------")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"invites"))

    print(
        f'{bot.user} is connected to {len(bot.guilds)} guilds\n'
    )
    for x in bot.guilds:
        print ("-")
        print(f'{x.name}(id: {x.id})')
        print(f'Guild Members:{x.member_count}')
        
    print ("------------------------------------")
    print(f"{bcolors.PURPLE}Started in {round(time.time()-start,2)} seconds.{bcolors.ENDC}\n")

    for guild in bot.guilds:
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

bot.run(token)

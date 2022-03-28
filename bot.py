#!/usr/bin/env python3

import os
import re

from discord.ext import commands
from dotenv import load_dotenv

from .Modules._urlChecker import url_search

load_dotenv()

DISCORD_API = os.environ.get("DISCORD_API")

bot = commands.Bot(command_prefix='!')

# URL regex
# https://stackoverflow.com/questions/1410311/regular-expression-for-url-validation-in-javascript/1411800#1411800
# /(ftp|http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?/

@bot.event
async def on_ready():
    print("="*50)
    print('Im in, as {0.user}'.format(bot))
    print("="*50)

@bot.event
async def on_message(message):
    pass


bot.run(DISCORD_API)

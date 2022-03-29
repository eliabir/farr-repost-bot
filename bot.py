#!/usr/bin/env python3

import os

from dataclasses import dataclass
from datetime import datetime
from discord.ext import commands
from dotenv import load_dotenv

from .Modules._UrlChecker import url_check
from .Modules._DBreindex import refresh_db

load_dotenv()

DISCORD_API = os.environ.get("DISCORD_API")

bot = commands.Bot(command_prefix='!')

# URL regex
# https://stackoverflow.com/questions/1410311/regular-expression-for-url-validation-in-javascript/1411800#1411800
# /(ftp|http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?/

guild_name = "Emote"
last_db_refresh = datetime.now()

@bot.event
async def on_ready():
    print("="*50)
    print('Im in, as {0.user}'.format(bot))
    print("="*50)

@bot.event
async def on_message(message):
    if not message.guild == guild_name or message.bot:
        return

    urls = url_check(message)
    if not urls:
        return

    


@bot.command
async def db_reindex(ctx):
    current_time = datetime.now()
    time_delta = current_time - last_db_refresh

    if time_delta.seconds > 60**2:
        refresh_db(bot.guilds)
        await ctx.send("Refreshed message database.")
    else:
        time_left = 60**2 - time_delta.seconds
        if time_left > 60:
            time_left_unit = "minutes"
            time_left = time_left//60
        else:
            time_left_unit = "seconds"

        await ctx.send(f"Less than 1 hour since last refresh. Wait {time_left} more {time_left_unit}.")
        return


bot.run(DISCORD_API)

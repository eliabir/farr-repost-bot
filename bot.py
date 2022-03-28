#!/usr/bin/env python3

import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

DISCORD_API = os.environ.get("DISCORD_API")

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("="*50)
    print('Im in, as {0.user}'.format(bot))
    print("="*50)



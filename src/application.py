# application.py

import asyncio
import io
import aiohttp
import re
import random
import discord
import time
import os
from dotenv import load_dotenv
from sys import argv
from discord.ext import tasks
from discord.ext import commands

from models.client import Client
from functions.getDiscordToken import getDiscordToken

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()  # All but the two privileged ones
intents.members = True  # Subscribe to the Members intent

asyncio.set_event_loop(asyncio.new_event_loop())
client = Client(command_prefix='!', intents=intents)
client.run(TOKEN)

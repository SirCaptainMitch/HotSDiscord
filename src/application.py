import asyncio
import io
import aiohttp
import re
import random
import discord
import time
from sys import argv
from discord.ext import tasks
from discord.ext import commands

from models.client import Client
from functions.getDiscordToken import getDiscordToken

# char=[[247677408386351105,'<:GoToChar:793111041046609951>',time.time()],[129702871837966336,'<:tww2:793399028611285022>',time.time()]]#[ID, emoji, time]
char = []

# global exitBool
# exitBool=0
# while not exitBool: #Restart
# 	exitBool=1
intents = discord.Intents.default()  # All but the two privileged ones
intents.members = True  # Subscribe to the Members intent

asyncio.set_event_loop(asyncio.new_event_loop())
client = Client(command_prefix='!', intents=intents)
client.run(getDiscordToken())

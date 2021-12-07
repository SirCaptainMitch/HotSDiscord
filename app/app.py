import asyncio
import discord
import os
from dotenv import load_dotenv
from sys import argv

# custom import
from app.models.client import Client
from app.db import create_database
from app.models.user import User


def run():
    load_dotenv()

    session = create_database()
    user = User('TheCaptain', '176118079942688770')

    session.add(user)

    TOKEN = os.getenv('DISCORD_TOKEN')

    intents = discord.Intents.default()  # All but the two privileged ones
    intents.members = True  # Subscribe to the Members intent

    asyncio.set_event_loop(asyncio.new_event_loop())
    client = Client(command_prefix='!', intents=intents)
    client.run(TOKEN)



if __name__ == '__main__':    
    run()

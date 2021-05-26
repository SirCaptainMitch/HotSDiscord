from app.functions.players import * 
import os 

from dotenv import load_dotenv
playersPath = './app/data/players.json'
load_dotenv()
players = get_players(playersPath)

print(players)

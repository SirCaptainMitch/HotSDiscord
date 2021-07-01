from app.functions.roster import * 
import os 
import json 
import pandas as pd
from dotenv import load_dotenv


playersPath = './app/data/players.json'
rosterPath = './app/data/roster.json'

load_dotenv()

def on_ready(playersPath, rosterPath): 
  # load_roster(playersPath, rosterPath)
  players = get_roster(playersPath)
  df = pd.DataFrame(players)
  print(df)

on_ready(playersPath, rosterPath)

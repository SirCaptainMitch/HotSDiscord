import json
from app.models.player import Player
import requests as req
import os

def get_players(path): 
  playerList = []
  TOKEN = os.getenv('HEROES_PROFILE_TOKEN')
  API_URL = os.getenv('API_URL')

  with open(path, 'r', encoding='utf8') as f:
      players = json.load(f)

  for player in players:
    playerUrl = '{api_url}/Player/?api_token={token}&region=1&battletag={full_battletage}'.format(
    api_url = API_URL,
    token = TOKEN,
    full_battletage = player['full_battletag']
    )
    res = req.get(playerUrl)
    player_content = json.loads(res.content)
    player = Player(
      blizz_id = player_content["blizz_id"],
      battletag = player_content["battletag"],
      region = player_content["region"],
      profile = player_content["profile"]
    ) 
    players.append(player)

    return players


def load_players(path):
  get_players(path)
  playerList = []
  with open(path, 'wb', encoding='utf8') as f:
      players = json.dumps(f)


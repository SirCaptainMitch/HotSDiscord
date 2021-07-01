import json
import asyncio
from app.models.player import Player
import requests as req
import os

## This will be converted to a Roster Class, but for now its easier to do it as a helper function

def load_roster(path, rosterPath): 
  playerList = []
  TOKEN = os.getenv('HEROES_PROFILE_TOKEN')
  API_URL = os.getenv('API_URL')
  playerUrl = '{api_url}/Player/?api_token={token}&region=1&battletag={full_battletag}'
  playerMMRUrl = '{api_url}/Player/MMR?api_token={token}&mode=json&battletag={full_battletag}&region=1'

  with open(path, 'r', encoding='utf8') as f:
    players = json.load(f)

  for player in players:
    url = playerUrl.format(
    api_url = API_URL,
    token = TOKEN,
    full_battletag = player['full_battletag']
    )

    res = req.get(url)
    player_content = json.loads(res.content)

    url = playerMMRUrl.format(
    api_url = API_URL,
    token = TOKEN,
    full_battletag = player['full_battletag']
    )

    res = req.get(url)
    mmr_content = json.loads(res.content)

    for k,v in mmr_content.items():
      # json.loads(p)
      # print(type(p))
      print(v["Quick Match"]["mmr"])

    player = Player(
      blizz_id = player_content["blizz_id"],
      battletag = player_content["battletag"],
      full_battletag = player["full_battletag"],
      region = player_content["region"],
      profile = player_content["profile"],
      qm_mmr = mmr_content["Quick Match"]["mmr"],
      qm_games_played = mmr_content["Quick Match"]["games_played"],
      qm_games_played_last_90_days = mmr_content["Quick Match"]["games_played_last_90_days"],
      qm_league_tier = mmr_content["Quick Match"]["league_tier"],
      urd_mmr = mmr_content["Unranked Draft"]["mmr"],
      urd_games_played = mmr_content["Unranked Draft"]["games_played"],
      urd_games_played_last_90_days = mmr_content["Unranked Draft"]["games_played_last_90_days"],
      urd_league_tier = mmr_content["Unranked Draft"]["league_tier"],
      hl_mmr = mmr_content["Hero League"]["mmr"],
      hl_games_played = mmr_content["Hero League"]["games_played"],
      hl_games_played_last_90_days = mmr_content["Hero League"]["games_played_last_90_days"],
      hl_league_tier = mmr_content["Hero League"]["league_tier"],
      tl_mmr = mmr_content["Team League"]["mmr"],
      tl_games_played = mmr_content["Team League"]["games_played"],
      tl_games_played_last_90_days = mmr_content["Team League"]["games_played_last_90_days"],
      tl_league_tier = mmr_content["Team League"]["league_tier"],
      sl_mmr = mmr_content["Storm League"]["mmr"],
      sl_games_played = mmr_content["Storm League"]["games_played"],
      sl_games_played_last_90_days = mmr_content["Storm League"]["games_played_last_90_days"],
      sl_league_tier = mmr_content["Storm League"]["league_tier"],
    ) 
    playerList.append(json.loads(player.json()))
  
  with open(rosterPath, "w") as outfile:
      json.dump(playerList, outfile,  indent=4, sort_keys=True)
      outfile.close()


def get_roster(path):
  playerList = [] 
  with open(path, 'r', encoding='utf8') as f:
      playerList = json.load(f)
  
  return playerList

# def load_roster_mmr(rosterPath):
#     TOKEN = os.getenv('HEROES_PROFILE_TOKEN')
#     API_URL = os.getenv('API_URL')

#     with open(rosterPath, 'r', encoding='utf8') as f:
#       players = json.load(f)

#     playerMMRUrl = '{api_url}/Player/MMR?api_token={token}&mode=json&battletag={full_battletag}&region=1'

#     for player in players:
#       url = playerMMRUrl.format(
#     api_url = API_URL,
#     token = TOKEN,
#     full_battletag = player['full_battletag']
#     )

#     res = req.get(playerMMRUrl)
#     player_content = json.loads(res.content)
#     player = Player(      
#       blizz_id = player_content["blizz_id"],
#       battletag = player_content["battletag"],
#       region = player_content["region"],
#       profile = player_content["profile"]
#     ) 
#     # playerList.append(json.loads(player.json()))

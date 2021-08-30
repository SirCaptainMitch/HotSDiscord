import json 

class Alias: 
  def __init__(self, obj):
    self.Hero = obj["hero"]
    self.HeroAliasList = obj["aliases"]
    self.AbilityAliasList = obj["abilityAliases"]

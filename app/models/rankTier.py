import json
from app.functions.helper import Helper

class RankTier(object):
  def __init__(self, **kwargs):
    for key, value in kwargs.items():
            setattr(self, key, Helper(key, value))

  def json(self):
      '''Helper method to dump instance to json
      '''
      obj = {}
      for attr in dir(self):
          if isinstance(getattr(self, attr), Helper):
              obj[attr] = getattr(self, attr).value
      return json.dumps(obj)

  def set_attr(self, **kwargs):
    for key, value in kwargs.items():
            setattr(self, key, Helper(key, value))

  def get_mmr_tiers(self):
    

    return { 
      "mmr": self.mmr,
      "rank": self.rank
    }



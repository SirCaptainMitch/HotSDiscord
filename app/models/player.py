import json
from app.models.helper import Helper

class Player(object):
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



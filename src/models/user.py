class Hero(object):
    def __init__(self, userName, discordId ):        
        self.UserName = userName
        self.DiscordId = discordId
    
    def toDict(self): 
      return self.__dict__

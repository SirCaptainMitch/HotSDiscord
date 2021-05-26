from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    UserName = Column(String)
    DiscordId = Column(String)

    def __init__(self, userName, discordId):
        self.UserName = userName
        self.DiscordId = discordId


    def __repr__(self):
       return "UserName='{userName}', DiscordId='{discordId}'".format(userName = self.UserName, discordId=self.DiscordId)


def getDiscordToken():
  with open('./config/token.txt', 'r') as file:
    token = file.read()
  return token


if __name__=='__main__':
	getDiscordToken()
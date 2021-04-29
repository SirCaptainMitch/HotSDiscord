def getProbiusToken():
  with open('./config/token.txt', 'r') as file:
    token = file.read()
  return token
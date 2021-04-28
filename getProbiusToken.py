def getProbiusToken():
  with open('./token.txt', 'r') as file:
    token = file.read()
  return token
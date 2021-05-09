class Hero(object):
    def __init__(self, heroInfo, gamemode):
        # Name, winrate, popularity, banrate, games played
        self.gamemode = gamemode
        [self.name, heroInfo] = heroInfo.split('win_rate')
        [self.wr, heroInfo] = heroInfo.split('popularity')
        if gamemode == 'qm':
            [self.pop, self.games] = heroInfo.split('games_played')
        else:
            [self.pop, heroInfo] = heroInfo.split('ban_rate')
            [self.br, self.games] = heroInfo.split('games_played')
            self.brChange = 0
        self.ci = str(
            round(1.96*(float(self.wr)*(100-float(self.wr))/int(self.games))**0.5, 2))
        self.name = shortenName(self.name)

    def heroString(self):
        if len(self.pop) == 3:
            self.pop += '0'
        if len(self.ci) == 3:
            self.ci += '0'
        if self.gamemode == 'qm':
            return(self.name+' '*(10-len(self.name))+self.wr+'  ±'+self.ci+'  '+self.pop)
        else:
            return(self.name+' '*(12-len(self.name))+self.wr+' ±'+self.ci+' '*(4-len(self.br))+self.br+' '*(7-len(self.pop))+self.pop+' '*(9-len(self.games))+self.games)

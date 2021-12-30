from urllib.request import urlopen
from app.functions.aliases import *
from app.functions.printFunctions import getHeroes

quotes_path = r'./data/quotes.json'

def getQuote(hero):

    hero_lower = hero.lower()
    with open(quotes_path, 'r') as f:
        quotes = json.loads(f.read())

    quote_string = "**{hero}:** {quote}"

    for obj in quotes:
        if hero_lower == obj["hero"].lower():
            hero_name = obj["hero"].replace('_', ' ')
            return quote_string.format(hero=hero_name, quote=obj["quote"])

    return ''


def downloadQuotes():
    noQuoteOnPage = ['Anduin', 'Imperius', 'Mephisto', 'Murky', 'Probius', 'Qhira', 'The_Butcher', 'Whitemane']
    theirQuote = ['For the Alliance above all!', 'I yearn for battle.', '*(Hisses)*', 'Mrrgll', '*(Probe sounds)*',
                  "I'm in.", 'Fresh meat!', 'Let the inquisition commence!']
    with open('quotes.txt', 'w+') as f:
        for hero in getHeroes():
            hero = aliases(hero)
            if hero in noQuoteOnPage:
                quote = theirQuote[noQuoteOnPage.index(hero)]
            else:
                page = ''.join(
                    [i.strip().decode('utf-8') for i in urlopen('https://heroesofthestorm.gamepedia.com/' + hero)])
                page = page[page.index('<p><i>"') + 7:]
                quote = page[:page.index('"')]
            output = hero + '; ' + quote
            f.write(output + '\n')


if __name__ == '__main__':
    downloadQuotes()

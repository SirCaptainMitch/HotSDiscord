import json

# quotes_path = r'../heroConfig/quotes.txt'
quotes_path = r'../app/data/quotes.json'

def getQuote(hero):
    with open(quotes_path, 'r') as f:
        for line in f:
            if hero.replace('ú', 'u') in line:
                return '**' + hero.replace('_', ' ') + ':** ' + line[line.index('; ') + 2:]
        return ''


def getQuoteJson(hero):

    hero_lower = hero.lower()
    with open(quotes_path, 'r') as f:
        quotes = json.loads(f.read())

    quote_string = "**{hero}:** {quote}"

    for obj in quotes:
        if hero_lower == obj["hero"].lower():
            hero_name = obj["hero"].replace('_', ' ')
            return quote_string.format(hero=hero_name, quote=obj["quote"])

        return ''


    # quote = (quote for quote in quotes if quotes["hero"] == hero).__next__()

    # return quote


hero_search = 'ch'

# print(getQuote(hero_search))
print(getQuoteJson(hero_search))

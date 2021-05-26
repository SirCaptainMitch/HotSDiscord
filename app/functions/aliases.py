from app.models.alias import Alias
import json

allHeroes = {
        'bruiser': ['Artanis', 'Chen', 'D.Va', 'Deathwing', 'Dehaka', 'Gazlowe', 'Hogger', 'Imperius', 'Leoric', 'Malthael', 'Ragnaros', 'Rexxar', 'Sonya', 'Thrall', 'Varian', 'Xul', 'Yrel'],
        'healer': ['Alexstrasza', 'Ana', 'Anduin', 'Auriel', 'Brightwing', 'Deckard', 'Kharazim', 'Li_Li', 'Lt._Morales', 'Lúcio', 'Malfurion', 'Rehgar', 'Stukov', 'Tyrande', 'Uther', 'Whitemane'],
        'mage': ['Azmodan', 'Chromie', 'Gall', "Gul'dan", 'Jaina', "Kael'thas", "Kel'Thuzad", 'Li-Ming', 'Mephisto', 'Nazeebo', 'Orphea', 'Probius', 'Tassadar'],
        'marksman': ['Cassia', 'Falstad', 'Fenix', 'Genji', 'Greymane', 'Hanzo', 'Junkrat', 'Lunara', 'Nova', 'Raynor', 'Sgt._Hammer', 'Sylvanas', 'Tracer', 'Tychus', 'Valla', 'Zagara', "Zul'jin"],
        'melee': ['Alarak', 'Illidan', 'Kerrigan', 'Maiev', 'Murky', 'Qhira', 'Samuro', 'The_Butcher', 'Valeera', 'Zeratul'],
        'support': ['Abathur', 'Medivh', 'The_Lost_Vikings', 'Zarya'],
        'tank': ["Anub'arak", 'Arthas', 'Blaze', 'Cho', 'Diablo', 'E.T.C.', 'Garrosh', 'Johanna', "Mal'Ganis", 'Mei', 'Muradin', 'Stitches', 'Tyrael']
}


def getHeroes():  # Returns an alphabetically sorted list of all allHeroes.
    return sorted([j for i in allHeroes.values() for j in i])


def aliasTrim(hero):
    return hero.lower().replace('_', '').replace('.', '').replace(' ', '').replace("'", "").replace('-', '').replace('[', '').replace('\n', '')


def loadAliases(path):
    heroList = []
    with open(path, 'r', encoding='utf8') as f:
        aliases = json.load(f)

    [heroList.append(Alias(x)) for x in aliases]
    return heroList


def aliases(hero):
    hero = aliasTrim(hero)
    heroList = loadAliases('./app/data/aliases.json')

    for x in heroList:
      if hero in x.HeroAliasList:
        return x.Hero.replace(' ', '_')

    for i in getHeroes():
        if hero in aliasTrim(i):
            return i


def abilityAliases(hero, name):  # Spell hero with correct capitalization, then rest lowercase
    if hero == 'Ana':
        if name == 'nanoboost':
            return 'nano boost'
    elif hero == 'Anduin':
        if name == 'lifegrip':
            return 'leap of faith'
    elif hero == 'Azmodan':
        if name in ['sieging wrath']:
            return 'demonic invasion'
    elif hero == 'Cassia':
        if name in ['volleyball', 'tetherball']:
            return 'ball lightning'
    elif hero == 'Fenix':
        if name in ['aiur noon']:
            return 'purification salvo'
    elif hero == 'Genji':
        if name in ['dblade']:
            return 'dragonblade'
        elif name in ['dc', 'claw']:
            return 'dragon claw'
    elif hero == 'Hanzo':
        if name == 'potg':
            return 'play of the game'
    elif hero == 'Leoric':
        if name == 'spooky hand':
            return 'drain hope'
    elif hero == 'Lúcio':
        if name == 'boop':
            return 'soundwave'
    elif hero == 'Lt._Morales':
        if name == 'stimdrone':
            return 'stim drone'
    elif hero == 'Malfurion':
        if name in ['broccoli']:
            return 'vengeful roots'
    elif hero == 'Ragnaros':
        if name in ['meatball']:
            return 'living meteor'
    elif hero == 'Samuro':
        if name in ['pta', 'press the advantage']:
            return 'press'
        elif name in ['mcs']:
            return 'merciless'
        elif name in ['wotw']:
            return 'way of the wind'
        elif name in ['woi']:
            return 'way of illusion'
        elif name in ['wotb']:
            return 'way of the blade'
        elif name in ['owtw']:
            return 'one with the wind'
        elif name in ['pp']:
            return 'phantom pain'
        elif name in ['bb']:
            return 'burning blade'
        elif name in ['cb']:
            return 'crushing blows'
        elif name in ['im']:
            return 'illusion master'
        elif name in ['bs']:
            return 'bladestorm'
        elif name in ['ms']:
            return 'mirrored steel'
        elif name in ['sh']:
            return 'shukuchi'
        elif name in ['kw']:
            return 'kawarimi'
        elif name in ['hw']:
            return 'harsh winds'
        elif name in ['dod']:
            return 'dance of death'
        elif name in ['tbs', '3bs']:
            return 'three blade style'
        elif name in ['ws']:
            return 'wind strider'
        elif name in ['bmp']:
            return 'pursuit'
    elif hero == 'Tyrael':
        if name in ['swordhole']:
            return 'sword of justice'
        if name in ['judgement']:
            return 'judgment'
    elif hero == 'Zeratul':
        if name in ['za warudo', 'vp']:
            return 'void prison'
    return name

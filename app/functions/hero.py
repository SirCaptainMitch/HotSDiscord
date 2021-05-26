import random

from app.data.commands import *
from app.data.discordIDs import *
from app.functions.emojis import emoji
from app.functions.draft import draft
from app.functions.aliases import *
from app.functions.miscFunctions import *
from app.functions.builds import *
from app.functions.printFunctions import *
from app.functions.heroesTalents import *
from app.functions.quotes import *
from app.functions.maps import *

drafts = {}
lastDraftMessageDict = {}
draftNames = {}

def heroCommand():

    hero = command
    hero = aliases(hero)
    output = ''
    # Patch notes have abilities in []. Don't want spammed triggers again. Numbers for R1, R2, etc.
    if len(hero) == 1 or (len(hero) == 2 and ('1' in hero or '2' in hero)):
        return 

    if len(text) == 2:  # If user switches to hero first, then build/quote
        if text[1] in buildsAliases:
            await guide(hero, message.channel)
            continue
        if text[1] in quotesAliases and text[1] != 'q':
            await message.channel.send(getQuote(hero))
            continue
        if text[1] in heroStatsAliases:
            await heroStats(hero, message.channel)
            continue
    try:
        (abilities, talents) = client.heroPages[hero]
    except:
        try:
            await printAll(client, message, text[0])
        except:
            pass
        continue

    try:
        # If there is no identifier, then it throws exception
        tier = text[1]
        if tier in randomAliases:
            await message.channel.send(printTier(talents, random.randint(0, 6)))
            return
    except:
        quote = getQuote(hero)
        output = '\n'.join(abilities)
        await printLarge(message.channel, quote+output)
        await heroStats(hero, message.channel)
        continue
    if output == '':
        if tier.isdigit():  # Talent tier
            tier = int(tier)
            # Talents for Chromie come 2 lvls sooner, except lvl 1
            output = printTier(talents, int(tier/3)+int(hero ==
                                                        'Chromie' and tier not in [1, 18]))
        elif tier in ['mount', 'z']:
            await message.channel.send(printAbility(abilities, 'z'))
            return
        elif tier == 'extra':
            await message.channel.send(printAbility(abilities, '1'))
            return
        elif tier == 'r':  # Ultimate
            if hero == 'Tracer':  # She starts with her heroic already unlocked, and only has 1 heroic
                output = abilities[3]
            else:
                output = printTier(talents, 3-2*int(hero == 'Varian')
                                   )  # Varian's heroics are at lvl 4
                if hero == 'Deathwing':
                    # Deathwing has Cataclysm baseline
                    output = abilities[3]+'\n'+output
        elif len(tier) == 1 and tier in 'dqwe':  # Ability (dqwe)
            output = printAbility(abilities, tier)
        elif tier == 'trait':
            output = printAbility(abilities, 'd')
        elif tier in wikipageAliases:  # Linking user to wiki instead of printing everything
            await message.channel.send('<https://heroesofthestorm.gamepedia.com/Data:'+hero+'#Skills>')
            continue
        else:
            output = await printSearch(abilities, talents, tier, hero, True)

    if len(output) == 2:  # If len is 2, then it's an array with output split in half
        if message.channel.name == 'rage':
            await message.channel.send(output[0].upper())
            await message.channel.send(output[1].upper())
        else:
            await message.channel.send(output[0])
            await message.channel.send(output[1])
    else:
        if message.channel.name == 'rage':
            output = output.upper()
        try:
            await message.channel.send(output)
        except:
            if output == '':
                try:  # If no results, it's probably an emoji with : forgotten. Prefer to call with : to avoid loading abilities and talents page
                    await emoji(client, [hero, tier], message.channel)
                    continue
                except:
                    pass
                if message.channel.name == 'rage':
                    await message.channel.send('ERROR: {} DOES NOT HAVE "{}".'.format(hero, tier).upper())
                else:
                    await message.channel.send('Error: {} does not have "{}".'.format(hero, tier))
                print('No results')
            else:
                if message.channel.name == 'rage':
                    await printLarge(message.channel, output.upper())
                else:
                    await printLarge(message.channel, output)

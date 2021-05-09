import asyncio
import io
import aiohttp
import re
import random
import discord
import time
from sys import argv
from discord.ext import tasks
from discord.ext import commands

from data.commands import *
from data.discordIDs import *
from functions.emojis import emoji
from functions.draft import draft
from functions.aliases import *
from functions.miscFunctions import *
from functions.builds import *
from functions.printFunctions import *
from functions.heroesTalents import *
from functions.quotes import *
from functions.maps import * 


drafts = {}
lastDraftMessageDict = {}
draftNames = {}


async def main(client, message, texts):
		global exitBool
		for draftAlias in draftAliases:
				if 'new' in message.content.lower():
						continue
				if '['+draftAlias+'/' in message.content.lower():
						break
		else:
				channelName = message.channel.name
				loggingMessage = channelName + ' ' + ' '*(17-len(channelName)) + str(
						message.author.name) + ' '*(18-len(str(message.author.name))) + ' ' + message.content
				# print(loggingMessage)
				await client.get_channel(DiscordChannelIDs['LoggingChannel']).send('`{}`'.format(loggingMessage))

		for text in texts:
				command = text[0].replace(' ', '')
				if command in ['trait', 'r', 'w', 'e', 'passive', 'react', '...']:
						print(1)
						continue
				if command in ['event', 'season']:
						print(2)
						await event(message.channel)
						continue
				if command in ['armor', 'armour', 'ehp']:
						print(3)
						await message.channel.send('https://cdn.discordapp.com/attachments/741762417976934460/801905601809612821/unknown.png')
						continue
				if command == 'hoggerangles':
						print(4)
						await message.channel.send('https://editor.p5js.org/Asddsa76/sketches/CmGYMS2j1')
						continue
				if command in ['schedule', 'patchschedule']:
						print(5)
						await schedule(message)
						continue
				if command == 'sortlist':
						print(6)
						await sortList(message)
						continue
				if command in heroAliases+[i+'s' for i in heroAliases]:						
						print(7)
						await heroes(message, text, message.channel, client)
						continue
				if command == 'ping':
						print(8)
						await ping(message.channel)
						continue
				if command == 'membercount':
						print(9)
						await memberCount(message.channel)
						continue
				if command in confidenceAliases:
						print(10)
						await confidence(message.channel, text)
						continue
				if command == 'exit' and message.author.id == DiscordUserIDs['TheCaptain']:
						print(11)
						exitBool = 1
						await client.close()
				if command in restartAliases:
						print(12)
						exitBool = 0
						await client.logout()
				if command in mapImageAliases:
						print(13)
						await mapImage(message.channel, text[1])
						continue
				if command == 'core':
						print(14)
						await coreAbilities(message.channel, await mapAliases(text[1]))
						continue
				if command in listAliases:
						print(15)
						await waitList(message, text, client)
						continue
				if command in lfgAlises:
						print(16)
						await lfg(message.channel, text[1], client)
						continue
				# if command in deleteAliases:
				# 		print(17)
				# 		await deleteMessages(message.author, text[1], client)
				# 		continue
				if command in patchNotesAliases:
						print(18)
						await patchNotes(message.channel, text)
						continue
				if command in talentAliases:
						print(19)
						await message.channel.send("Call a hero's talent tier with [hero/level]")
						continue
				if command in rollAliases:
						print(20)
						await roll(text, message)
						continue
				if command == 'sort':
						print(21)
						await sortFromMessage(text[1], message, client)
						continue
				if command == ':disapproval':
						print(22)
						await message.channel.send('ಠ_ಠ')
						continue
				if command == ':summon':
						print(23)
						if len(text) == 1:
								await message.channel.send('༼ つ ◕\_◕ ༽つ')
						elif '@' in text[1]:
								await message.channel.send('{0} {0} Summon {1}! {0} {0}'.format('༼ つ ◕\_◕ ༽つ', message.author.mention))
						else:
								# text[1] is all lowercase etc.
								await message.channel.send('{0} {0} Summon {1}! {0} {0}'.format('༼ つ ◕\_◕ ༽つ', message.content.split('[')[1].split('/')[1].split(']')[0]))
						continue
				if command in colourAliases:
						print(24)
						await message.channel.send(file=discord.File('WS colours.png'))
						continue
				if message.author.id == DiscordUserIDs['TheCaptain']:
						if command == 'repeat' and len(text) == 2:
								await message.channel.send(text[1])
								await message.delete()
								continue
				if command == 'vote':
						print(26)
						await vote(message, text)
						continue
				if command in coinsAliases:
						print(27)
						await message.channel.send(random.choice(['Heads', 'Tails']))
						continue
				if command in redditAliases:
						print(28)
						await reddit(client, message, text)
						continue
				if command in ['avatar', 'a']:
						print(29)
						await message.channel.send(await getAvatar(client, message.channel, text[1]))
						continue
				if command == '':
						print(30)
						continue
				if command in draftAliases:
						print(31)
						await draft(drafts, message.channel, message.author, text, lastDraftMessageDict, draftNames)
						continue
				if command in randomAliases:
						print(32)
						if len(text) == 1:
								await message.channel.send(getQuote(random.choice(getHeroes())))
								continue
						command = random.choice(getHeroes())
				if command in helpAliases:
						print(33)
						if len(text) == 2 and command in heroStatsAliases:  # [info/hero]
								await heroStats(aliases(text[1]), message.channel)
						else:
								await message.channel.send(helpMessage())
						continue
				if command in buildsAliases:
						print(34)
						if len(text) == 2:
								await message.channel.send("Elitesparkle's builds: <https://elitesparkle.wixsite.com/hots-builds>")
						continue
				if command in rotationAlises:
						print(35)
						await rotation(message.channel)
						continue
				if command == 'goodbot':
						print(36)
						await emoji(client, ['Probius', 'love'], message.channel)
						continue
				if command == 'badbot':
						print(37)
						if message.author.id in ProbiusPrivilegesIDs:
								await emoji(client, ['Probius', 'sad'], message.channel)
						else:
								await emoji(client, [':pylonbat'], message.channel)
						continue
				if ':' in command:
						print(38)
						await emoji(client, text, message.channel, message)
						continue
				if ']' in command:
						print(39)
						continue
				if command in ['chogall', "cho'gall", 'cg', 'cho gall', 'cho-gall']:
						print(40)
						await message.channel.send("Cho and Gall are 2 different heroes. Choose one of them")
						print('Dual hero')
						continue
				if command in quotesAliases:
						print(41)
						if len(text) == 2:
								await message.channel.send(getQuote(aliases(text[1])))
						# Calling [q] alone shouldn't show link, but [q/hero] works, as well as [quotes]
						elif text[0] != 'q':
								await message.channel.send('All hero select quotes: <https://github.com/Asddsa76/Probius/blob/master/quotes.txt>')
						continue
				if command in aliasesAliases:
						print(42)
						await message.channel.send('All hero alternate names: <https://github.com/Asddsa76/Probius/blob/master/aliases.py>')
						continue
				if command == 'all':
						print(43)
						await printAll(client, message, text[1], True)
						continue
				if command in emojiAliases:
						print(44)
						await message.channel.send('Emojis: [:hero/emotion], where emotion is of the following: happy, lol, sad, silly, meh, angry, cool, oops, love, or wow.')
						continue
				try:
						# [t3221323,sam]						
						if len(text) == 1 and command[0] == 't' and command[8] == ',':
								await printBuild(client, message.channel, command)
								continue
						# [t3221323/sam]
						if len(text) == 2 and command[0] == 't' and len(command) == 8 and command != 'tassadar':
								await printBuild(client, message.channel, ','.join(text))
								continue
				except:
						pass
				hero = command
				# Patch notes have abilities in []. Don't want spammed triggers again. Numbers for R1, R2, etc.
				if len(hero) == 1 or (len(hero) == 2 and ('1' in hero or '2' in hero)):
						print(45)
						continue
				hero = aliases(hero)
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

				output = ''
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

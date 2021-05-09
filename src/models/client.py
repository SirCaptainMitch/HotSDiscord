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

from functions.reddit import *
from functions.findTexts import *
from functions.main import *
from functions.heroesTalents import *
from functions.maps import * 


class Client(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.seenTitles = []
        self.seenPosts = []
        self.forwardedPosts = []
        self.proxyEmojis = {}
        # create the background task and run it in the background
        self.bgTask0 = self.loop.create_task(self.bgTaskSubredditForwarding())
        self.heroPages = {}
        self.lastWelcomeImage = []
        self.waitList = []
        self.ready = False  # Wait until ready before taking commands
        self.rulesChannel = None
        self.welcomeMessage = ''

    async def on_ready(self):
        print('Logged on...')
        print('Filling up with Reddit posts...')
        self.forwardedPosts = []
        self.seenTitles = await fillPreviousPostTitles(self)
        print('Downloading heroes...')
        await downloadAll(self, argv)
        self.ready = True
        print('Ready!')
        # self.rulesChannel=self.get_channel(DiscordChannelIDs['ServerRules'])#server-rules

    async def on_message(self, message):
        if message.embeds and message.channel.id == DiscordChannelIDs['General'] and 'View tweet' in message.content:
            await message.channel.send(message.embeds[0].thumbnail.url)
            await message.edit(suppress=True)
        # Blizztrack posts in general
        if message.author.id == 272526395337342977 and message.channel.id == DiscordChannelIDs['General']:
            try:
                e = message.embeds[0].fields[3]
                if e.name == 'Full patch notes at':
                    output = 'Patch notes!\n'+e.value
                    await message.channel.send('@everyone '+output)
                    await self.get_channel(222817241249480704).send(output)
            except:
                print('here')
                pass
        if message.author.bot:  # Don't respond to bots
            return
        if self.ready == False:
            return
        elif '[' in message.content:
            texts = findTexts(message)
            await main(self, message, texts)

        await removeEmbeds(message)
        if message.author.id == 0:  # Birthday cake
            await message.add_reaction('🍰')

    async def on_message_edit(self, before, after):
        if after.embeds and after.channel.id == DiscordChannelIDs['General'] and 'New dev tweet!' in after.content:
            await after.channel.send(after.embeds[0].thumbnail.url)
            await after.edit(suppress=True)
        if before.author.bot:
            return
        if '[' in after.content:
            try:
                beforeTexts = findTexts(before)
            except:
                beforeTexts = []
            newTexts = [i for i in findTexts(after) if i not in beforeTexts]
            if newTexts:
                await main(self, after, newTexts)

        await removeEmbeds(after)
        if '<@' in after.content:
            if '@here' in after.content or '@everyone' in after.content:
                await after.channel.send(after.author.mention+'<:bonk:761981366744121354>')
                return
            newMentions = [i for i in findMentions(
                after) if i not in findMentions(before)]
            if newMentions:
                await after.channel.send(', '.join(newMentions)+', '+after.author.display_name+' wants to ping you!')

    async def on_raw_reaction_add(self, payload):
        member = self.get_user(payload.user_id)
        if member.id == DiscordUserIDs['Probius']:
            return
        try:
            message = await self.get_channel(payload.channel_id).fetch_message(payload.message_id)
        except:
            return
        if message.author.id == 670832046389854239:  # Advisor wrote message
            return
        # Message is from Probius, and is downvoted with thumbs down
        elif message.author.id == DiscordUserIDs['Probius'] and str(payload.emoji) == '👎':
            # Message is in reddit posts
            if message.channel.id in [DiscordChannelIDs['RedditPosts']]:
                output = member.mention+'<:bonk:761981366744121354>'
                # await self.get_channel(DiscordChannelIDs['General']).send(output)#general
                return
            elif 'reddit.com' in message.content:
                await message.channel.send(member.mention+'<:bonk:761981366744121354>')
                return
            elif '<:bonk:761981366744121354>' in message.content or '@' in message.content:
                return
            output = member.name+' deleted a message from Probius'
            print(output)
            await self.get_channel(DiscordChannelIDs['LoggingChannel']).send('`'+output+'`')
            await message.delete()
            return
        elif message.author.id == DiscordUserIDs['Probius'] and 'React to ping' in message.content and str(payload.emoji) == '👍':
            output = member.name+' started a balance discussion'
            print(output)
            await self.get_channel(DiscordChannelIDs['LoggingChannel']).send('`'+output+'`')
            return
        elif str(payload.emoji) == '⚽' and message.channel.id == DiscordChannelIDs['General']:
            await sortFromReaction(message, member.id, self)
            return
        if member.id in ProbiusPrivilegesIDs:
            await message.add_reaction(payload.emoji)

    async def on_raw_reaction_remove(self, payload):
        member = self.get_user(payload.user_id)
        try:
            message = await self.get_channel(payload.channel_id).fetch_message(payload.message_id)
        except:
            pass
        return

    async def on_member_join(self, member):
        print('test')
        channel = self.get_channel(DiscordChannelIDs['General'])
        self.welcomeMessage = 'Welcome {} !'.format(member.name)
        return self.welcomeMessage.append(await channel.send('/giphy hello there'))

    async def on_member_remove(self, member):
        member = self.get_user(payload.user_id)
        try:
            message = await self.get_channel(payload.channel_id).fetch_message(payload.message_id)
        except:
            pass
        # await self.get_channel(DiscordChannelIDs['LoggingChannel']).send('`{loggingMessage} left {channel}`'.format(loggingMessage = loggingMessage, channel = member.channelName))
        # return

    async def bgTaskSubredditForwarding(self):
        await self.wait_until_ready()
        channel = self.get_channel(DiscordChannelIDs['General'])
        while not self.is_closed():
            await asyncio.sleep(60)  # Check for new posts every minute
            try:
                await redditForwarding(self)
            except:
                pass

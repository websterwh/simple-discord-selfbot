from asyncio.tasks import sleep
from typing import ContextManager, Text
import discord
from discord import message
from discord import channel
from discord.embeds import Embed, EmptyEmbed
from discord.ext import commands
import json
import os
import logging
from os import system
import asyncio
import cfonts
import dhooks
from dhooks import Webhook
import random
import requests
from random import randint
from requests.api import delete
import colorama
from colorama import Fore
import datetime
import time


with open('config.json') as cjson:
    config = json.load(cjson)
    token = config.get('token')
    botprefix = config.get('prefix')


os.system('cls')

bot = commands.Bot(command_prefix=botprefix, self_bot = True, fetch_offline_members=True, guild_subscriptions = True, help_command=None, intents=intents)

@bot.command('sendembed')
async def sendembed(ctx, *, arg):
    await ctx.message.delete()
    embed = discord.Embed(description=arg, color='000000')
    await ctx.send(embed=embed)
    

@bot.command()
async def cum(ctx, editDelay:int=1):
    await ctx.message.delete()
    msg = await ctx.send("""
:ok_hand:          :smile:
   :eggplant: :zzz: :necktie: :eggplant:
                :oil:     :nose:
                :zap: 8=:punch:=D
         :trumpet:      :eggplant:
    """)
    await asyncio.sleep(editDelay)
    await msg.edit(content="""
:ok_hand:          :smiley:
   :eggplant: :zzz: :necktie: :eggplant:
                :oil:     :nose:
                :zap: 8==:punch:D
         :trumpet:      :eggplant:
    """)
    await asyncio.sleep(editDelay)
    await msg.edit(content="""
:ok_hand:          :grimacing:
   :eggplant: :zzz: :necktie: :eggplant:
                :oil:     :nose:
                :zap: 8=:punch:=D
         :trumpet:      :eggplant:
    """)
    await asyncio.sleep(editDelay)
    await msg.edit(content="""
:ok_hand:          :persevere:
   :eggplant: :zzz: :necktie: :eggplant:
                :oil:     :nose:
                :zap: 8==:punch:D
         :trumpet:      :eggplant:
    """)
    await asyncio.sleep(editDelay)
    await msg.edit(content="""
:ok_hand:          :confounded:
   :eggplant: :zzz: :necktie: :eggplant:
                :oil:     :nose:
                :zap: 8=:punch:=D
         :trumpet:      :eggplant:
    """)
    await asyncio.sleep(editDelay)
    await msg.edit(content="""
:ok_hand:          :tired_face:
   :eggplant: :zzz: :necktie: :eggplant:
                :oil:     :nose:
                :zap: 8==:punch:D
         :trumpet:      :eggplant:
    """)
    await asyncio.sleep(editDelay)
    await msg.edit(content="""
:ok_hand:          :weary:
   :eggplant: :zzz: :necktie: :eggplant:
                :oil:     :nose:
                :zap: 8=:punch:= D:sweat_drops:
         :trumpet:      :eggplant:
    """)
    await asyncio.sleep(editDelay)
    await msg.edit(content="""
:ok_hand:          :dizzy_face:
   :eggplant: :zzz: :necktie: :eggplant:
                :oil:     :nose:
                :zap: 8==:punch:D :sweat_drops:
         :trumpet:      :eggplant:                 :sweat_drops:
    """)
    await asyncio.sleep(editDelay)
    await msg.edit(content="""
:ok_hand:          :drooling_face:
   :eggplant: :zzz: :necktie: :eggplant:
                :oil:     :nose:
                :zap: 8==:punch:D :sweat_drops:
         :trumpet:      :eggplant:                 :sweat_drops:
    """)

@bot.command('test')
async def test(ctx, *, arg):
    await ctx.message.delete()
    msg = await ctx.send(arg)
    await asyncio.sleep(1)
    await msg.edit(content='working')

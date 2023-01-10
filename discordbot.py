from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
import asyncio
from discord.ui import Button, View
from discord.ext import commands
from discord.utils import get

load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

page1 = discord.Embed(title="추천 사냥터 (LV.1-100)", description="**1~30**\n ```새비지 터미널 - 들개들의 싸움터1```\n **30~50**\n ```테마던전 - 골드비치```\n **50~60** ```슬리피우드 - 조용한 습지```\n **60~70** ```오르비스 - 하늘계단1```\n **70~90** ```아리안트 - 사헬지대1```\n **90~100** ```마가티아 - 관계자 외 출입금지```", colour=0xffc0cb)
page2 = discord.Embed(title="추천 사냥터 (LV.100-200)", description="**100~110**\n ```리프레 - 하늘 둥지 2```\n **110~140**\n ```시계탑 - 잊혀진 회랑``````폐광 - 시련의 동굴 1,2,3``````아랫마을 - 도깨비집```\n **150~160**\n", colour=0xffc0cb)
page3 = discord.Embed(title="Bot Help 3", description="Page 3", colour=0xffc0cb)

bot.help_pages = [page1, page2, page3]


@bot.event
async def on_ready():
    print(f'Logged in as {client.user}.')


@bot.command()
async def yeah(ctx):
    buttons = [u"\u23EA", u"\u2B05", u"\u27A1", u"\u23E9"] # skip to start, left, right, skip to end
    current = 0
    msg = await ctx.send(embed=bot.help_pages[current])
    
    for button in buttons:
        await msg.add_reaction(button)
        
    while True:
        try:
            reaction, user = await bot.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=3612361283193.0)

        except asyncio.TimeoutError:
            return print("test")

        else:
            previous_page = current
            if reaction.emoji == u"\u23EA":
                current = 0
                
            elif reaction.emoji == u"\u2B05":
                if current > 0:
                    current -= 1
                    
            elif reaction.emoji == u"\u27A1":
                if current < len(bot.help_pages)-1:
                    current += 1

            elif reaction.emoji == u"\u23E9":
                current = len(bot.help_pages)-1

            for button in buttons:
                await msg.remove_reaction(button, ctx.author)

            if current != previous_page:
                await msg.edit(embed=bot.help_pages[current])

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")

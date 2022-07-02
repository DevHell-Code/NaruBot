import discord
from discord.ext import commands
import os
import asyncio
import random
import re
import uptimes.uptimes
import time
from discord_slash import cog_ext, SlashCommand,SlashContext
from discord_slash.utils.manage_commands import create_option,create_choice
import datetime


# 임배드 함수
def embed(title, description, color=random.randint(0x000000, 0xFFFFFF)):
    return discord.Embed(title=title, description=description, color=color)


class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        if not hasattr(bot, "slash"):
            bot.slash = SlashCommand(
                bot,
                auto_register=True,
                override_type=True,
                auto_delete=True,
            )

        self.bot.slash.get_cog_commands(self)
    @cog_ext.cog_slash(name="업타임")
    async def _uptime(self, ctx: SlashContext):
        nowtime = uptimes.uptimes()
        odays = nowtime.split(' ')[0]
        ohours = nowtime.split(' ')[2]
        omin = nowtime.split(' ')[4]
        osec = nowtime.split(' ')[6]
    
        days = odays[2:len(odays)-2]
        hours = ohours[2:len(ohours)-2]
        minutes = omin[2:len(omin)-2]
        seconds = osec[2:len(osec)-2]
        await ctx.send(embed=embed("업타임",f'저는 {days}일, {hours}시간 {minutes}분 {seconds}초 동안 작동됐어요!'))
    # 정보
    @commands.command()
    async def 정보(self, ctx):
        await ctx.reply(embed=embed(
            '정보',
            'Ver. INDEV 7 \n Made By Dev HellCode, Github: https://github.com/DevHell-Code/Hell-Bot'
        ))

    # 정보
    @commands.command()
    async def 정보(self, ctx):
        await ctx.reply(embed=embed(
            '정보',
            'Ver. INDEV 7 \n Made By Dev HellCode, Github: https://github.com/DevHell-Code/Hell-Bot'
        ))

      
    # 크레딧
    @commands.command()
    async def 크레딧(self, ctx):
        await ctx.reply(embed=embed(
            '크레딧', 'Dev HellCode \n froggal(KeySpace), hminkoo10(Kongryeong)'))

    # 연락
    @commands.command()
    async def 연락(self, ctx):
        await ctx.reply(embed=embed(
            '연락처',
            'Dev HellCode\n`froggal`(KeySpace)에게 연락: `Discord: froggal#2188` \n `Email: keyfroggal21k@hellcode.cf` \n `hyminkoo10`(Kongryeong)에게 연락: `Discord: Kongryeong#5252`\n `Email: kongryeong@hellcode.cf` \n ``'
        ))
    # 초대 코드
    @commands.command()
    async def 초대(self, ctx):
        invite = 'https://hellcode.cf/naru'
        await ctx.reply(embed=embed('초대 링크', f'{invite} 링크를 사용하세요.'))

    @commands.command()
    async def 업타임(self,ctx):
        nowtime = uptimes.uptimes()
        odays = nowtime.split(' ')[0]
        ohours = nowtime.split(' ')[2]
        omin = nowtime.split(' ')[4]
        osec = nowtime.split(' ')[6]
    
        days = odays[2:len(odays)-2]
        hours = ohours[2:len(ohours)-2]
        minutes = omin[2:len(omin)-2]
        seconds = osec[2:len(osec)-2]
        await ctx.send(embed=embed("업타임",f'저는 {days}일, {hours}시간 {minutes}분 {seconds}초 동안 작동됐어요!'))
    @cog_ext.cog_slash(name="핑")
    async def _ping(self,ctx:SlashContext):
        time1 = time.time()
        if (round(self.bot.latency*1000)) > 150:
                embed = discord.Embed(color=0x00ff00)
                embed = discord.Embed(title=":ping_pong:퐁!", description="""
                현재 디스코드 api핑: {0}ms
                상태: 매우 나쁨:no_entry:""".format(round(self.bot.latency*1000)), color=0xff0000)
        if (round(self.bot.latency*1000)) < 100:
                embed = discord.Embed(color=0x00ff00)
                embed = discord.Embed(title=":ping_pong:퐁!", description="""
                현재 디스코드 api핑: {0}ms
                상태: 양호:white_check_mark:""".format(round(self.bot.latency*1000)), color=0x00ff00)
        if (round(self.bot.latency*1000)) < 50:
                embed = discord.Embed(color=0x00ff00)
                embed = discord.Embed(title=":ping_pong:퐁!", description="""
                현재 디스코드 api핑: {0}ms
                상태: 매우 좋음:green_heart:""".format(round(self.bot.latency*1000)), color=0x0000ff)
        await ctx.send(embed=embed)
    @commands.command()
    async def 핑(self,ctx):
        time1 = time.time()
        if (round(self.bot.latency*1000)) > 150:
                embed = discord.Embed(color=0x00ff00)
                embed = discord.Embed(title=":ping_pong:퐁!", description="""
                현재 디스코드 api핑: {0}ms
                상태: 매우 나쁨:no_entry:""".format(round(self.bot.latency*1000)), color=0xff0000)
        if (round(self.bot.latency*1000)) < 100:
                embed = discord.Embed(color=0x00ff00)
                embed = discord.Embed(title=":ping_pong:퐁!", description="""
                현재 디스코드 api핑: {0}ms
                상태: 양호:white_check_mark:""".format(round(self.bot.latency*1000)), color=0x00ff00)
        if (round(self.bot.latency*1000)) < 50:
                embed = discord.Embed(color=0x00ff00)
                embed = discord.Embed(title=":ping_pong:퐁!", description="""
                현재 디스코드 api핑: {0}ms
                상태: 매우 좋음:green_heart:""".format(round(self.bot.latency*1000)), color=0x0000ff)
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Core(bot))

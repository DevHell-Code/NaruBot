import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash import SlashContext
from discord_slash.utils import manage_commands
import random
import asyncio
import os
import base64
import urllib
import requests
import time
from bs4 import BeautifulSoup
from discord_slash import SlashCommand
from discord_slash import SlashContext
from discord_slash.utils import manage_commands
from discord.utils import get
import re

class Naru(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        slash = SlashCommand(bot, sync_commands=True)
    @commands.command()
    async def status(ctx,address):
        maker=requests.get(f"https://api.mcsrvstat.us/2/{address}")
        output=maker.json()
        if output["online"] is not True:
            return await ctx.reply("서버가 오프라인입니다")
        res = requests.get(f'https://mcsrvstat.us/server/{address}')
        soup = BeautifulSoup(res.content, 'html.parser')
        serverinf = soup.findAll('span', 'badge bg-info')
        imgUrl = soup.find("img","d-none d-sm-block")["src"]
        svinf = []
        for i in serverinf:
            svinf.append(i.get_text())
        embed = discord.Embed(title=f"{address}'s status", color=random.randint(0x000000,0xFFFFFF))
        embed.add_field(name='Server Domain', value=f"{svinf[0]}", inline=False)
        embed.add_field(name='Server Ip', value=f"{svinf[1]}", inline=False)
        embed.add_field(name='Server Port', value=f"{svinf[2]}", inline=False)
        embed.add_field(name='Protocol Version', value=f"{svinf[3]}", inline=False)
        embed.add_field(name='Server Version', value=output["version"], inline=False)
        motd = output["motd"]["clean"]
        m = "\n"
        for i in motd:
            m = m + f'{i}\n'
        embed.add_field(name='Server motd', value=m, inline=False)
        player = str(output["players"]["online"]) + " / " + str(output["players"]["max"])
        embed.add_field(name='Player', value=player, inline=False)
        try:
            data = requests.get(f"https://api.minetools.eu/ping/{address}").json()
            player = f"{data['players']['sample']}"
            p = []
            u = []
            for i in eval(player):
                p.append(i["name"])
                u.append(i["id"])
            pl = "``"
            n = 0
            for i in eval(player):
                pl = f"{pl}{str(p[n])} ({str(u[n])}), "
                n =+ 1
            pl = f"``{pl}``"
            if pl == "````":
                pl = "too many players!"
            embed.add_field(name='Player List', value=pl, inline=False)
            embed.set_thumbnail(url=f"https://api.mcsrvstat.us/icon/{address}")
            embed.set_footer(text=f'{ctx.author} 님이 명령어를 사용함', icon_url=ctx.author.avatar_url)
            await ctx.reply(embed=embed)
        except:
            embed.set_thumbnail(url=f"https://api.mcsrvstat.us/icon/{address}")
            embed.set_footer(text=f'{ctx.author} 님이 명령어를 사용함', icon_url=ctx.author.avatar_url)
            await ctx.reply(embed=embed)
    @slash.slash(
      name = 'status',
      options=[manage_commands.create_option(
        name = "address",
        description='확인할 JE 1.4+ 서버/BE 서버 주소(IP).',
        option_type = 3,
        required = True
      )]
    )
    async def check(ctx:SlashContext, address:str):
        await ctx.send(content="추출중입니다. 잠시만 기다려주세요",hidden=True)
        maker=requests.get(f"https://api.mcsrvstat.us/2/{address}")
        output=maker.json()
        if output["online"] is not True:
            return await ctx.send("서버가 오프라인입니다",hidden=True)
        res = requests.get(f'https://mcsrvstat.us/server/{address}')
        soup = BeautifulSoup(res.content, 'html.parser')
        serverinf = soup.findAll('span', 'badge bg-info')
        imgUrl = soup.find("img","d-none d-sm-block")["src"]
        svinf = []
        for i in serverinf:
            svinf.append(i.get_text())
        embed = discord.Embed(title=f"{address}'s status", color=random.randint(0x000000,0xFFFFFF))
        embed.add_field(name='Server Domain', value=f"{svinf[0]}", inline=False)
        embed.add_field(name='Server Ip', value=f"{svinf[1]}", inline=False)
        embed.add_field(name='Server Port', value=f"{svinf[2]}", inline=False)
        embed.add_field(name='Protocol Version', value=f"{svinf[3]}", inline=False)
        embed.add_field(name='Server Version', value=output["version"], inline=False)
        motd = output["motd"]["clean"]
        m = "\n"
        for i in motd:
            m = m + f'{i}\n'
        embed.add_field(name='Server motd', value=m, inline=False)
        player = str(output["players"]["online"]) + " / " + str(output["players"]["max"])
        embed.add_field(name='Player', value=player, inline=False)
        try:
            data = requests.get(f"https://api.minetools.eu/ping/{address}").json()
            player = f"{data['players']['sample']}"
            p = []
            u = []
            for i in eval(player):
                p.append(i["name"])
                u.append(i["id"])
            pl = "``"
            n = 0
            for i in eval(player):
                pl = f"{pl}{str(p[n])} ({str(u[n])}), "
                n =+ 1
            pl = f"{pl}``"
            if pl == "````":
                pl = "too many players!"
            embed.add_field(name='Player List', value=pl, inline=False)
            embed.set_thumbnail(url=f"https://api.mcsrvstat.us/icon/{address}")
            embed.set_footer(text=f'{ctx.author} 님이 명령어를 사용함', icon_url=ctx.author.avatar_url)
            await ctx.reply(embed=embed)
        except:
            embed.set_thumbnail(url=f"https://api.mcsrvstat.us/icon/{address}")
            embed.set_footer(text=f'{ctx.author} 님이 명령어를 사용함', icon_url=ctx.author.avatar_url)
            await ctx.reply(embed=embed)
    @commands.command()
    async def player(ctx, player):
        res = requests.get(f'https://minecraftuuid.com/?search={player}')
        soup = BeautifulSoup(res.content, 'html.parser')
        uuid = soup.findAll("input","Form-Control")
        plinf = []
        for i in uuid:
            plinf.append(i["value"])
        playernames = [f"```\n{plinf[0]}\n"]
        try:
            n = plinf[3].split(',')
            for i in n:
                playernames.append(f"{i}\n")
            playernames.append("```")
            historyname = ""
            for i in playernames:
                historyname = historyname + i
        except:
            historyname = player
        historyname = historyname.replace(" ","")
        embed = discord.Embed(title=f"{player}'s Information", color=random.randint(0x000000,0xFFFFFF))
        embed.add_field(name='Player UUID', value=f"{plinf[1]}", inline=False)
        embed.add_field(name='Player Name History', value=f"{historyname}", inline=False)
        command113 = '/give @p minecraft:player_head{SkullOwner:"playernamereplacespot"}'
        embed.add_field(name='Player Skull Command (equal or bigger than 1.13)', value=f"{command113.replace('playernamereplacespot',player)}", inline=False)
        command112 = '/give @p minecraft:skull 1 3 {SkullOwner:"playernamereplacespot"}'
        embed.add_field(name='Player Skull Command (equal or smaller than 1.12)', value=f"{command112.replace('playernamereplacespot',player)}", inline=False)
        embed.set_footer(text=f'{ctx.author} 님이 명령어를 사용함', icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=embed)
    @slash.slash(
      name = 'player',
      options=[manage_commands.create_option(
        name = "playername",
        description='JE Player Name',
        option_type = 3,
        required = True
      )]
    )
    async def checkplayer(ctx:SlashContext, playername:str):
        await ctx.send(content="추출중입니다. 잠시만 기다려주세요",hidden=True)
        res = requests.get(f'https://minecraftuuid.com/?search={playername}')
        soup = BeautifulSoup(res.content, 'html.parser')
        uuid = soup.findAll("input","Form-Control")
        plinf = []
        for i in uuid:
            plinf.append(i["value"])
        playernames = [f"```\n{plinf[0]}\n"]
        try:
            n = plinf[3].split(',')
            for i in n:
                playernames.append(f"{i}\n")
            playernames.append("```")
            historyname = ""
            for i in playernames:
                historyname = historyname + i
        except:
            historyname = playername
        historyname = historyname.replace(" ","")
        embed = discord.Embed(title=f"{playername}'s Information", color=random.randint(0x000000,0xFFFFFF))
        embed.add_field(name='Player UUID', value=f"{plinf[1]}", inline=False)
        embed.add_field(name='Player Name History', value=f"{historyname}", inline=False)
        command113 = '/give @p minecraft:player_head{SkullOwner:"playernamereplacespot"}'
        embed.add_field(name='Player Skull Command (equal or bigger than 1.13)', value=f"{command113.replace('playernamereplacespot',playername)}", inline=False)
        command112 = '/give @p minecraft:skull 1 3 {SkullOwner:"playernamereplacespot"}'
        embed.add_field(name='Player Skull Command (equal or smaller than 1.12)', value=f"{command112.replace('playernamereplacespot',playername)}", inline=False)
        embed.set_footer(text=f'{ctx.author} 님이 명령어를 사용함', icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=embed)
    
    @commands.command()
    async def tetrio(ctx,player):
        maker=requests.get(f"https://ch.tetr.io/api/users/{player}/")
        output=maker.json()
        if output["success"] is False:
            await ctx.send("플래이어 이름을 다시 확인해주세요")
            return
        userinfo = output["data"]["user"]
        embed = discord.Embed(title=f"{player}'s Information", color=random.randint(0x000000,0xFFFFFF))
        __id = output["data"]["user"]["_id"]
        embed.add_field(name='Player Id', value=f"{__id}", inline=False)
        if userinfo['country'] is not None:
            country = f":flag_{userinfo['country'].lower()}:"
        else:
            country = "None"
        embed.add_field(name="Player's Country", value=f"{country}", inline=False)
        joineddate = output["data"]["user"]["ts"].split("T")[0]
        embed.add_field(name='Player Joined date', value=f"{joineddate}", inline=False)
        playtime = int(int(userinfo["gametime"]) // 3600)
        embed.add_field(name='Play Time', value=f"{playtime} Hours", inline=False)
        embed.add_field(name='Friends Count', value=f"{userinfo['friend_count']}", inline=False)
        embed.add_field(name='Number of Games Played', value=f"{userinfo['gamesplayed']}", inline=False)
        embed.add_field(name='Number of Games Won', value=f"{userinfo['gameswon']}", inline=False)
        embed.add_field(name='Number of Games Played - Tetra League', value=f"{userinfo['league']['gamesplayed']}", inline=False)
        embed.add_field(name='Number of Games Won - Tetra League', value=f"{userinfo['league']['gameswon']}", inline=False)
        maker=requests.get(f"https://ch.tetr.io/api/users/{player}/records/")
        output=maker.json()
        try:
            line40 = output["data"]["records"]["40l"]
            line40record = int(line40["record"]["endcontext"]["finalTime"] / 60000 * 60)
            embed.add_field(name='40 Line Record', value=f"{line40record} Seconds", inline=False)
            line40recordeddate = line40["record"]["ts"].split("T")[0]
            embed.add_field(name='40 Line Record', value=f"{line40recordeddate}", inline=False)
            line40replayid = line40["record"]["replayid"]
            embed.add_field(name='40 Line Record Replay', value=f"[Replay](https://tetr.io/#r:{line40replayid})", inline=False)
        except:
            pass
        try:
            blitz = output["data"]["records"]["blitz"]
            blitzrecord = int(blitz["record"]["endcontext"]["score"])
            embed.add_field(name='Blitz Record', value=f"{blitzrecord}", inline=False)
            blitzrecordeddate = blitz["record"]["ts"].split("T")[0]
            embed.add_field(name='Blitz Record', value=f"{blitzrecordeddate}", inline=False)
            blitzreplayid = blitz["record"]["replayid"]
            embed.add_field(name='Blitz Record Replay', value=f"[Replay](https://tetr.io/#r:{blitzreplayid})", inline=False)
        except:
            pass
        embed.set_thumbnail(url=f"https://tetr.io/user-content/avatars/{__id}.jpg")
        embed.set_footer(text=f'{ctx.author} 님이 명령어를 사용함', icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=embed)
    
    @slash.slash(
      name = 'tetrio',
      options=[manage_commands.create_option(
        name = "player",
        description="tetr.io player name",
        option_type = 3,
        required = True
      )]
    )
    async def tetris(ctx:SlashContext, player:str):
        maker=requests.get(f"https://ch.tetr.io/api/users/{player}/")
        output=maker.json()
        if output["success"] is False:
            await ctx.send("플래이어 이름을 다시 확인해주세요")
            return
        userinfo = output["data"]["user"]
        embed = discord.Embed(title=f"{player}'s Information", color=random.randint(0x000000,0xFFFFFF))
        __id = output["data"]["user"]["_id"]
        embed.add_field(name='Player Id', value=f"{__id}", inline=False)
        if userinfo['country'] is not None:
            country = f":flag_{userinfo['country'].lower()}:"
        else:
            country = "None"
        embed.add_field(name="Player's Country", value=f"{country}", inline=False)
        joineddate = output["data"]["user"]["ts"].split("T")[0]
        embed.add_field(name='Player Joined date', value=f"{joineddate}", inline=False)
        playtime = int(int(userinfo["gametime"]) // 3600)
        embed.add_field(name='Play Time', value=f"{playtime} Hours", inline=False)
        embed.add_field(name='Friends Count', value=f"{userinfo['friend_count']}", inline=False)
        embed.add_field(name='Number of Games Played', value=f"{userinfo['gamesplayed']}", inline=False)
        embed.add_field(name='Number of Games Won', value=f"{userinfo['gameswon']}", inline=False)
        embed.add_field(name='Number of Games Played - Tetra League', value=f"{userinfo['league']['gamesplayed']}", inline=False)
        embed.add_field(name='Number of Games Won - Tetra League', value=f"{userinfo['league']['gameswon']}", inline=False)
        maker=requests.get(f"https://ch.tetr.io/api/users/{player}/records/")
        output=maker.json()
        try:
            line40 = output["data"]["records"]["40l"]
            line40record = int(line40["record"]["endcontext"]["finalTime"] / 60000 * 60)
            embed.add_field(name='40 Line Record', value=f"{line40record} Seconds", inline=False)
            line40recordeddate = line40["record"]["ts"].split("T")[0]
            embed.add_field(name='40 Line Record', value=f"{line40recordeddate}", inline=False)
            line40replayid = line40["record"]["replayid"]
            embed.add_field(name='40 Line Record Replay', value=f"[Replay](https://tetr.io/#r:{line40replayid})", inline=False)
        except:
            pass
        try:
            blitz = output["data"]["records"]["blitz"]
            blitzrecord = int(blitz["record"]["endcontext"]["score"])
            embed.add_field(name='Blitz Record', value=f"{blitzrecord}", inline=False)
            blitzrecordeddate = blitz["record"]["ts"].split("T")[0]
            embed.add_field(name='Blitz Record', value=f"{blitzrecordeddate}", inline=False)
            blitzreplayid = blitz["record"]["replayid"]
            embed.add_field(name='Blitz Record Replay', value=f"[Replay](https://tetr.io/#r:{blitzreplayid})", inline=False)
        except:
            pass
        embed.set_thumbnail(url=f"https://tetr.io/user-content/avatars/{__id}.jpg")
        embed.set_footer(text=f'{ctx.author} 님이 명령어를 사용함', icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=embed)

def setup(bot):
    bot.add_cog(Naru(bot))
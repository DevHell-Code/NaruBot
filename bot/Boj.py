import discord
from discord.ext import commands
import random
from baekjoon import boj


# 임배드 함수
def embed(title, description, color=random.randint(0x000000, 0xFFFFFF)):
    return discord.Embed(title=title, description=description, color=color)


class Boj(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 백준(self, ctx, name):
        await ctx.reply(embed=embed(
            'Boj Profile',
            f'아이디 {boj.get_status_message(name)} \n 랭크 : {boj.get_rank(name)} \n 맞은 문제들 : {boj.get_correct_qs(name)} \n 맞은 문제들의 개수 : {boj.get_correct_q(name)} \n 시도했지만 맞지 않은 문제들 : {boj.get_unsolved_qs(name)} \n 시도했지만 맞지 않은 문제의 개수 : {boj.get_unsolved_q(name)} \n 제출 개수 : {boj.get_submit_time(name)}'
        ))


def setup(bot):
    bot.add_cog(Boj(bot))

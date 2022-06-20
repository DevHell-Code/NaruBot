from discord.ext import commands
from discord_buttons_plugin import *

# 테스트입니다. 나중에 파일 삭제하시거나 다른곳으로 옮기셔도 됩니다.
# 참고 : https://www.youtube.com/watch?v=uphPkxy7p6k
# 안될때 pip install discord-buttons-plugin 하고 해보십쇼

# 버튼 세팅
buttons = ButtonsClient(bot)

@bot.command()
async def 버튼(ctx):
    await buttons.send(
        content = "아래쪽 버튼을 눌러주세요.", # 메시지
        channel = ctx.channel.id, # 채널
        components = [
            ActionRow([
                Button(
                    label="버튼입니다.", # 버튼에 표시될 이름
                    style=ButtonType().Primary, # 버튼 타입. 타입들은 https://url.kr/9ehb7f 참고.
                    # ButtonType().Primary (파란버튼)
                    # ButtonType().Success (초록버튼)
                    # ButtonType().Secondary (회색버튼)
                    # ButtonType().Danger (빨간버튼)
                    # ButtonType().Link (링크)
                    # ButtonType().Emoji (이모티콘) (되는지 테스트 안함)
                    custom_id="button_one" # 커스텀 아이디. async def button_one 에 사용할 수 있음.
                )
            ])
        ]
    )

@buttons.click
async def button_one(ctx):
    await ctx.reply("버튼이 눌렸습니다.") # 버튼이 눌렸을 때

def setup(bot):
    bot.add_cog(Button(bot))
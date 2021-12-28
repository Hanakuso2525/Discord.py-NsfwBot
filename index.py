try:
    import json
    from discord.ext import commands
    import discord, aiohttp
except ModuleNotFoundError:
    print("install.bat実行しました？？\n実行してないならしてくださいね")
    exit()

with open("config.json") as f:
    config = json.load(f)

bot = commands.Bot(
    command_prefix=config["prefix"],
    help_command=None,
    allowed_mentions=discord.AllowedMentions(replied_user=False),
)

R18_color = 0xff66b8
session = aiohttp.ClientSession()

async def neko_api_image(type: str):
    async with await session.get("https://nekobot.xyz/api/image?type=%s" % type) as res:
        res = await res.json()
    return res.get("message")

@bot.event
async def on_ready():
    print("起動完了！")

#おっぱい画像表示
@bot.command()
async def boobs(ctx):
    img = await neko_api_image("boobs")
    e = discord.Embed(title="R18画像", color=R18_color)
    e.set_image(url=img)
    await ctx.reply(embed=e)

#アナル画像表示
@bot.command()
async def anal(ctx):
    img = await neko_api_image("anal")
    e = discord.Embed(title="R18画像", color=R18_color)
    e.set_image(url=img)
    await ctx.reply(embed=e)

########他にもNekoAPIを使えば沢山の画像を取得できます。
########是非、NekoAPIのドキュメントを見て他にも沢山作ってみてください！！！
'''
img = await neko_api_image("anal")
ここの部分の "anal" のところをドキュメントで確認した画像IDに変更してみてください！
'''

if __name__ == "__main__":
    bot.run(config["Token"])

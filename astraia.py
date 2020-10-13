import discord
from discord.ext import commands
import sqlite3
import parse
import random
import aiohttp
from PIL import Image
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
BOT_CHANNEL = os.getenv('BOT_CHANNEL')

bot = commands.Bot(command_prefix='?')

@bot.command()
async def st0(ctx, *, name=None):
    if name is None or name.isspace():
        await ctx.send("곡 이름을 입력해 주세요.")
    else: await search_stella(0, ctx, name)

@bot.command()
async def st1(ctx, *, name=None):
    if name is None or name.isspace():
        await ctx.send("곡 이름을 입력해 주세요.")
    else: await search_stella(1, ctx, name)

@bot.command()
async def st2(ctx, *, name=None):
    if name is None or name.isspace():
        await ctx.send("곡 이름을 입력해 주세요.")
    else: await search_stella(2, ctx, name)

@bot.command()
async def st3(ctx, *, name=None):
    if name is None or name.isspace():
        await ctx.send("곡 이름을 입력해 주세요.")
    else: await search_stella(3, ctx, name)

@bot.command()
async def st4(ctx, *, name=None):
    if name is None or name.isspace():
        await ctx.send("곡 이름을 입력해 주세요.")
    else: await search_stella(4, ctx, name)

@bot.command()
async def st5(ctx, *, name=None):
    if name is None or name.isspace():
        await ctx.send("곡 이름을 입력해 주세요.")
    else: await search_stella(5, ctx, name)

@bot.command()
async def st6(ctx, *, name=None):
    if name is None or name.isspace():
        await ctx.send("곡 이름을 입력해 주세요.")
    else: await search_stella(6, ctx, name)

@bot.command()
async def st7(ctx, *, name=None):
    if name is None or name.isspace():
        await ctx.send("곡 이름을 입력해 주세요.")
    else: await search_stella(7, ctx, name)

@bot.command()
async def st8(ctx, *, name=None):
    if name is None or name.isspace():
        await ctx.send("곡 이름을 입력해 주세요.")
    else: await search_stella(8, ctx, name)

@bot.command()
async def st9(ctx, *, name=None):
    if name is None or name.isspace():
        await ctx.send("곡 이름을 입력해 주세요.")
    else: await search_stella(9, ctx, name)

@bot.command()
async def st10(ctx, *, name=None):
    if name is None or name.isspace():
        await ctx.send("곡 이름을 입력해 주세요.")
    else: await search_stella(10, ctx, name)

@bot.command()
async def st11(ctx, *, name=None):
    if name is None or name.isspace():
        await ctx.send("곡 이름을 입력해 주세요.")
    else: await search_stella(11, ctx, name)

@bot.command()
async def sl0(ctx, *, name=None):
    if name is None or name.isspace():
        await ctx.send("곡 이름을 입력해 주세요.")
    else: await search_satellite(0, ctx, name)

@bot.command()
async def sl1(ctx, *, name=None):
    if name is None or name.isspace():
        await ctx.send("곡 이름을 입력해 주세요.")
    else: await search_satellite(1, ctx, name)

@bot.command()
async def sl2(ctx, *, name=None):
    if name is None or name.isspace():
        await ctx.send("곡 이름을 입력해 주세요.")
    else: await search_satellite(2, ctx, name)

@bot.command()
async def sl3(ctx, *, name=None):
    if name is None or name.isspace():
        await ctx.send("곡 이름을 입력해 주세요.")
    else: await search_satellite(3, ctx, name)

@bot.command()
async def sl4(ctx, *, name=None):
    if name is None or name.isspace():
        await ctx.send("곡 이름을 입력해 주세요.")
    else: await search_satellite(4, ctx, name)

@bot.command()
async def sl5(ctx, *, name=None):
    if name is None or name.isspace():
        await ctx.send("곡 이름을 입력해 주세요.")
    else: await search_satellite(5, ctx, name)

@bot.command()
async def sl6(ctx, *, name=None):
    if name is None or name.isspace():
        await ctx.send("곡 이름을 입력해 주세요.")
    else: await search_satellite(6, ctx, name)

@bot.command()
async def sl7(ctx, *, name=None):
    if name is None or name.isspace():
        await ctx.send("곡 이름을 입력해 주세요.")
    else: await search_satellite(7, ctx, name)

@bot.command()
async def sl8(ctx, *, name=None):
    if name is None or name.isspace():
        await ctx.send("곡 이름을 입력해 주세요.")
    else: await search_satellite(8, ctx, name)

@bot.command()
async def sl9(ctx, *, name=None):
    if name is None or name.isspace():
        await ctx.send("곡 이름을 입력해 주세요.")
    else: await search_satellite(9, ctx, name)

@bot.command()
async def sl10(ctx, *, name=None):
    if name is None or name.isspace():
        await ctx.send("곡 이름을 입력해 주세요.")
    else: await search_satellite(10, ctx, name)

@bot.command()
async def sl11(ctx, *, name=None):
    if name is None or name.isspace():
        await ctx.send("곡 이름을 입력해 주세요.")
    else: await search_satellite(11, ctx, name)

@bot.command()
async def sl12(ctx, *, name=None):
    if name is None or name.isspace():
        await ctx.send("곡 이름을 입력해 주세요.")
    else: await search_satellite(12, ctx, name)

async def search_stella(level, ctx, name):
    conn = sqlite3.connect("Stellaverse.db")
    c = conn.cursor()
    t = (level, '%'+name+'%')
    c.execute('''SELECT st, name, artist, baseURL, sabunURL, LR2IR FROM stella WHERE st=? AND name LIKE ? COLLATE NOCASE''', t)
    l = c.fetchall()
    if len(l) > 1:
        msg = "검색 결과가 2개 이상 나왔습니다.\n```\n"
        for (i, s) in enumerate(l):
            level, name, artist, baseURL, sabunURL, LR2IR = s
            msg += name + "\n"
        msg += "```"
        await ctx.send(msg)
    elif len(l) == 1:
        level, name, artist, baseURL, sabunURL, LR2IR = l[0]
        embed=discord.Embed(title=name, url=LR2IR, description=artist, color=0x02bada)
        embed.set_author(name="st%d" % level,icon_url="https://stellabms.xyz/apple-icon.png")
        embed.add_field(name="本体URL", value=baseURL, inline=True)
        embed.add_field(name="差分URL", value=sabunURL, inline=True)
        await ctx.channel.send(embed=embed)
    else:
        await ctx.send("검색 결과가 없습니다.")
    conn.close()

async def search_satellite(level, ctx, name):
    conn = sqlite3.connect("Stellaverse.db")
    c = conn.cursor()
    t = (level, '%'+name+'%')
    c.execute('''SELECT sl, name, artist, baseURL, sabunURL, LR2IR FROM satellite WHERE sl=? AND name LIKE ? COLLATE NOCASE''', t)
    l = c.fetchall()
    if len(l) > 1:
        msg = "검색 결과가 2개 이상 나왔습니다.\n```\n"
        for (i, s) in enumerate(l):
            level, name, artist, baseURL, sabunURL, LR2IR = s
            msg += name + "\n"
        msg += "```"
        await ctx.send(msg)
    elif len(l) == 1:
        level, name, artist, baseURL, sabunURL, LR2IR = l[0]
        embed=discord.Embed(title=name, url=LR2IR, description=artist, color=0x02bada)
        embed.set_author(name="sl%d" % level,icon_url="https://stellabms.xyz/apple-icon.png")
        embed.add_field(name="本体URL", value=baseURL, inline=True)
        embed.add_field(name="差分URL", value=sabunURL, inline=True)
        await ctx.channel.send(embed=embed)
    else:
        await ctx.send("검색 결과가 없습니다.")
    conn.close()

@bot.command()
async def battle(ctx, *, arg=None):
    # 사용예시: st1, sl2
    if not arg:
        await ctx.send("사용예시: ```\n?battle st3\n?battle sl5\n```")
        return
    name = arg[:2]
    if name != 'st' and name != 'sl':
        await ctx.send("사용예시: ```\n?battle st3\n?battle sl5\n```")
        return
    level = 0
    try:
        level = int(arg[2:])
    except:
        await ctx.send("사용예시: ```\n?battle st3\n?battle sl5\n```")
    finally:
        conn = sqlite3.connect("Stellaverse.db")
        c = conn.cursor()
        t = (level, )
        if   name == 'sl': c.execute('''SELECT sl, name, artist, baseURL, sabunURL, LR2IR FROM satellite WHERE sl=?''', t)
        elif name == 'st': c.execute('''SELECT st, name, artist, baseURL, sabunURL, LR2IR FROM stella WHERE st=?''', t)
        l = c.fetchall()

        if len(l) < 1:
            await ctx.send(":warning: 그 레벨에는 차분이 존재 하지 않습니다.")
            return
        level, name, artist, baseURL, sabunURL, LR2IR = random.choice(l)
        embed=discord.Embed(title=name, url=LR2IR, description=artist, color=0x02bada)
        embed.set_author(name="sl%d" % level,icon_url="https://stellabms.xyz/apple-icon.png")
        embed.add_field(name="本体URL", value=baseURL, inline=True)
        embed.add_field(name="差分URL", value=sabunURL, inline=True)
        await ctx.channel.send(embed=embed)

@bot.event
async def on_message(msg):
    if msg.guild == bot.get_guild(BOT_CHANNEL):
        # See if a BMP file was sent
            if len(msg.attachments) > 0 and msg.attachments[0].url.endswith('.bmp'):
                # Start aiohttp session to retrieve the attachment image
                async with aiohttp.ClientSession() as session:
                    async with session.get(msg.attachments[0].url) as r:
                        if r.status == 200:
                            # Temporarily save the image as bmp
                            img_bytes = await r.read()
                            with open('temp.bmp', 'wb') as f: f.write(img_bytes)
                            # Convert bmp to png
                            img = Image.open('temp.bmp')
                            img.save('temp.png', 'png')
                            await msg.channel.send("{0}님이 업로드 하신 BMP 파일입니다.".format(msg.author.mention), file=discord.File('temp.png'))
                            await msg.delete()
    else:
        await bot.process_commands(msg)

@bot.event
async def on_ready():
    print("Astraia!")

if __name__ == "__main__":
    bot.run(os.getenv(TOKEN))
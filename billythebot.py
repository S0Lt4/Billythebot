import discord
from discord.ext import commands
import random, os
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
bot.run("token")
@bot.command(name="elisi_fikri")
async def elisi_fikri(ctx):
    ideas = [
        "Eski plastik şişelerden saksi yapabilirsiniz.",
        "Plastik kapaklardan küçük süs eşyaları yapabilirsiniz.",
        "Boş deterjan kutuların kullanarak saklama kutusu yapabilirsiniz.",
        "Plastik kaşık ve çatallardan dekoratif çerçeveler oluşturabilirsiniz."
    ]
    await ctx.send(f"İşte bir el işi fikri: {random.choice(ideas)}")

async def iyi_bilgiler(ctx):
    ideas = [
        "Eski plastik şişelerden saksi yapabilirsiniz.",
        "Plastik kapaklardan küçük süs eşyaları yapabilirsiniz.",
        "hi",
        "."
    ]
    await ctx.send(f"İşte bir el işi fikri: {random.choice(ideas)}")

async def mem(ctx):

    img_name = random.choice(os.listdir('billyphotos'))
    with open(f'billyphotos/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("TOKEN")

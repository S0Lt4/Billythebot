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
    information = [
        "Plastik; karbon (C), hidrojen (H), oksijen (O), azot (N) ve diğer organik ya da inorganik elementlerin oluşturduğu monomer adı verilen; basit yapıdaki moleküllü gruplardaki bağın koparılarak polimer adı verilen uzun ve zincirli bir yapıya dönüştürülmesi ile elde edilen malzemelere verilen isimdir.",
        "Petrol, milyonlarca yıl boyunca deniz canlılarının ve bitki kalıntılarının yer altında yüksek basınç ve sıcaklık altında dönüşmesiyle oluşan fosil bir yakıttır; enerji üretiminde, yakıt türlerinde (benzin, dizel) ve plastik gibi ürünlerin hammaddesi olarak yaygın şekilde kullanılır.",
        "Metal, yüksek elektrik ve ısı iletkenliği, parlak yüzeyi ve şekillendirilebilirliği ile bilinen, genellikle doğada cevher olarak bulunan ve sanayiden elektroniğe pek çok alanda kullanılan dayanıklı bir element grubudur.",
        "Karton ve kağıt, genellikle ağaç liflerinden üretilen ve geri dönüştürülebilir özellikleriyle çevre dostu malzemeler olup, kağıt yazı ve baskı için, karton ise daha kalın ve dayanıklı yapısıyla ambalajlama gibi alanlarda kullanılır."
    ]
    await ctx.send(f"iste guzel bir bilgi: {random.choice(information)}")

async def izlenicek_videolar(ctx):
    videolar = [
        "https://www.youtube.com/watch?v=aDCznz8rINY",
        "https://www.youtube.com/watch?v=RS7IzU2VJIQ",
        "https://www.youtube.com/watch?v=75d_29QWELk&t=4s"
    ]
    await ctx.send(f"iste isine yariya bilicek videolar: {random.choice(videolar)}")

async def mem(ctx):

    img_name = random.choice(os.listdir('billyphotos'))
    with open(f'billyphotos/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("TOKEN")

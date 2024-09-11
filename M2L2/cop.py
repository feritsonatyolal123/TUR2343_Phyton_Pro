from bot_token import token
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def kagit(ctx):
    await ctx.send('Kağıt geri dönüşüme gider. Kağıt atıkları: Kağıt, Karton, Kağıt Peçete, Defter(Belki)')

@bot.command()
async def plastik(ctx):
    await ctx.send('Plastik geri dönüşüme gider. Plastik atıkları: Pet Şişeler, Plastik kutular, plastik oyuncaklarlar, kısaca plastik olan herşey.')

@bot.command()
async def metal(ctx):
    await ctx.send('Metal geri dönüşüme gider. Metal Atıkları: Metal kutular, metal şişeler, konseve kutuları, çatal, bıçak, kaşık, aliminyum folyo, tava, çaydanlık.')

@bot.command()
async def cam(ctx):
    await ctx.send('Cam geri dönüşüme gider. Cam atıkları: Cam şişeler (Soda şişesi vb.), Bardak, Sürahi, Cam reçeller, cam kavanozlar.')

@bot.command()
async def ekstra(ctx):
    await ctx.send('Ekstramız ise pil! Pilleri belediye almıyor. Pilleri TAP(Taşınabilir Pil Üreticileri ve İthalatçıları Derneği) alıyordur.')

@bot.command()
async def geridonusumnedir(ctx):
    await ctx.send("""Geri dönüşüm kağıt, plastik, metal ve camları çöpe değilde geri dönüşüme atmakdır.
                    Geri dönüşüm kutularında birikince ya kurumlar yada belediye alır. 
                   Onları geri dönüşüm fabrikalarında geri dönüştürür. 
                   Yani kağıt kağıt hamuruna dönüştürülüp tekrardan kağıt olur ve böylece ağaç kesilmesini önler. 
                   Plastikler eritilip yine plastik olur. Camlarda aynnı metallerde. 
                   Kısaca geri dönüşüm yaparsak o malzemelerin daha az kullanılmasını sağlar.""")

bot.run(token)
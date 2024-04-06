import imp
import discord
from discord.ext import commands
import os
import random
import requests

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Dan inilah cara Kamu mengganti nama file dari variabel!
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
                    picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_fox_image_url():
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('fox')
async def fox(ctx):
    '''Setelah kita memanggil perintah fox (fox), program akan memanggil fungsi get_fox_image_url'''
    image_url = get_fox_image_url()
    await ctx.send(image_url)

organic = [
     'sisa makanan',
     'bahan kimia',
     'daun',
     'botol kertas',
     'kotoran hewan',
     'minyak bekas',
     'kertas', 
     'kayu',
     'batu',
     'minyak bumi'
]
anorganic = [
     'kaca',
     'stereofoam',
     'plastik',
     'barang elektronik',
     'kaleng alumunium',
     'besi',
     'karet'
]

@bot.command()
async def jenis_sampah(ctx):
     await ctx.send('Masukkan jenis sampah yang ingin kamu ketahui: ')
     msg = await bot.wait_for('message')
     if msg.content in organic:
          await ctx.send('Buang di tempat sampah ORGANIK😊')
     elif msg.content in anorganic:
          await ctx.send('Buang di tempat sampah ANORGANIK😊')
     elif msg.content not in anorganic or organic:
          await ctx.send('Maaf kami tidak menemukan barang itu🙏')

food = [
     'buah',
     'jeruk',
     'apel',
     'anggur',
     'pir',
     'nasi',
     'kurma',
     'semangka',
     'tulang',
     'sayur',
     'bayam',
     'kangkung',
     'daun',
]

plastic = [
     'ban bekas',
     'botol plastik',
     'plastik',
     'kantong plastik',
     'kresek',
     'gelas plastik',
     'mainan plastik',
     'meja plastik'
]

kertas = [
     'kertas',
     'gelas kertas',
     'tisu',
     'buku tulis',
     'buku gambar'
]

@bot.command()
async def umur_sampah(ctx):
     await ctx.send('Masukkan jenis sampah yang ingin kamu ketahui umurnya: ')
     msg = await bot.wait_for('message')
     if msg.content in food:
          await ctx.send('Rata-rata umurnya adalah 1 BULAN')
     elif msg.content in plastic:
          await ctx.send('Rata-rata umurnya adalah 1.000 TAHUN')
     elif msg.content in kertas:
          await ctx.send('Rata-rata umurnya adalah 2 - 6 BULAN')



bot.run("MTIxODQxNjQ4NTU1MTA1MDk0Mw.GRrJcZ.P-DiwdofdKmHQ2HGoCB0ynHcF4sJAkenSInXDk")


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}!'
            await guild.system_channel.send(to_send)


intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run('MTIxODQxNjQ4NTU1MTA1MDk0Mw.GRrJcZ.P-DiwdofdKmHQ2HGoCB0ynHcF4sJAkenSInXDk')
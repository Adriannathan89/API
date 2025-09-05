import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

dic_key = {"senin" : 0, "selasa" : 1, "rabu" : 2, "kamis" : 3, "jumat" : 4}
list_hari = ['Senin', "Selasa",  "Rabu", "Kamis", "Jumat"]

hasil_random = ['Untitled.jpeg', 'kaoruko.jpeg', 'waguri.jpeg']
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def foto(ctx, banyaknya: int = 10):
    await ctx.send(f'Nih {banyaknya} foto waifu lu bos')
    for i in range(banyaknya):
        await ctx.send(file=discord.File(random.choice(hasil_random)))

@bot.command()
async def jadwal(ctx, *, pesan):
    index = 0
    jadwal_sementara = [[], [], [], [], []]
    with open("jadwal.txt", "r") as f:
        content = f.readlines()
        
        for i in range(0, len(content)):
            tmp = content[i].lower().strip('\n')
            if tmp in dic_key:
                index = dic_key[tmp]
            elif('-' in content[i] and content[i] != '\n'):
                jadwal_sementara[index].append(content[i].strip('- ').strip('\n'))
    
    susunan_jadwal = pesan.split(', ')
    jadwal_sementara[dic_key[susunan_jadwal[0].lower()]].append(susunan_jadwal[1])
    with open('jadwal.txt', 'w') as x:
        for i in range(0, 5):
            x.write(list_hari[i] + '\n')
            for j in range(0, len(jadwal_sementara[i])):
                x.write('- ' + jadwal_sementara[i][j] + '\n')
            x.write("\n")
    await ctx.send(f"Jadwal untuk hari {susunan_jadwal[0].lower()} berhasil ditambahkan")

@bot.command()
async def liat_jadwal(ctx):
    with open("jadwal.txt", "r") as f:
        content = f.read()
        await ctx.send(content)

@bot.command()
async def clear_jadwal(ctx):
    with open('jadwal.txt', 'w') as f:
        for i in range(0, 5):
            f.write(list_hari[i] + '\n\n')
        await ctx.send('Jadwal berhasil dibersihkan')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 10):
    deleted = await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"🧹 Deleted {len(deleted)-1} messages", delete_after=3)

bot.run('MTQxMzE0ODA2MTc2ODYxMzkzOQ.Ga47P2.gRyy9jQLC3VWG9xHWt6bwYc2_NkciWf2GX6UY0')
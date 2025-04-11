import time
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as Test bot!')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a Test bot!')

@bot.command()
async def laugh(ctx, count_heh = 100):
    await ctx.send("he" * count_heh)

@bot.command()
async def smile(ctx):
    await ctx.send(f':D')

@bot.command()
async def repeat(ctx, times: int, content="Repeating on your command sir!"):
    for i in range(times):
        await ctx.send(content)

bot.run("Your token here :D")

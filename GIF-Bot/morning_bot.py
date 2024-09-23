import discord
import asyncio
from discord.ext import commands, tasks
from datetime import datetime, time, timezone, timedelta
import os


TOKEN = os.getenv('DISCORD_BOT_TOKEN')
TENOR_API_KEY = os.getenv('TENOR_API_KEY')

CHANNEL_ID =667399686998720516

GIF_LINK = 'https://tenor.com/view/goofy-gif-26077288'
SASCHA_LINK = 'https://tenor.com/view/zverev-gif-18040229'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

GIFS = {
    'Monday': 'Monday motivation',
    'Tuesday': 'Tuesday motivation',
    'Wednesday': 'Wednesday my dudes',
    'Thursday': 'Thursday vibes',
    'Friday': 'Friday feeling',
    'Saturday': 'Saturday',
    'Sunday': 'Sunday relaxation'
}

@tasks.loop(time=time(7, 0, tzinfo=timezone(timedelta(hours=2))))
async def send_morning_gif():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(GIF_LINK)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    send_morning_gif()
    channel =bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(GIF_LINK)
        await bot.close()


@bot.command(name='bruh')
async def send_bruh(ctx):
    await ctx.send(GIF_LINK)


@bot.command(name='Lucastinkt')
async def send_bruh(ctx):
    await ctx.send(SASCHA_LINK)


async def on_disconnect():
    print('Disconnected')

bot.run(TOKEN)

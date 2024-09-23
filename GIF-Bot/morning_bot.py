import random
import discord
import asyncio
from discord.ext import commands, tasks
from datetime import datetime, time, timezone, timedelta
import os
import requests


TOKEN = os.getenv('DISCORD_BOT_TOKEN')
TENOR_API_KEY = os.getenv('TENOR_API_KEY')

CHANNEL_ID =667399686998720516

GIF_LINK = 'https://tenor.com/view/goofy-gif-26077288'
SASCHA_LINK = 'https://tenor.com/view/zverev-gif-18040229'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

DAY_KEYWORDS = {
    'Monday': 'Monday motivation',
    'Tuesday': 'Tuesday motivation',
    'Wednesday': 'Wednesday my dudes',
    'Thursday': 'Thursday vibes',
    'Friday': 'Friday feeling',
    'Saturday': 'Saturday',
    'Sunday': 'Sunday relaxation'
}


def tenor_gif(keyword):
    url = f"https://tenor.googleapis.com/v2/search?q={keyword}&key={TENOR_API_KEY}&limit=10&media_filter=minimal"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("API Response:", data)
        gifs = data.get('results', [])
        if gifs:
            gif_index = random.randint(0, len(gifs) - 1)
            gif_url = gifs[gif_index]['media_formats']['gif']['url']
            print(f"Extracted GIF URL: {gif_url}")
            return gif_url
        else:
            print(f"No gifs found for {keyword}")
    else:
        print(f"Failed to fetch GIFs for keyword: {keyword}. Status Code: {response.status_code}")
    return None


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    channel = bot.get_channel(CHANNEL_ID)
    today = datetime.now().strftime('%A')
    keyword = DAY_KEYWORDS.get(today)
    gif_link = tenor_gif(keyword)
    if channel:
        if gif_link:
            try:
                await channel.send(gif_link)
            except Exception as e:
                print(f"Error sending message: {e}")
        else:
            print("No GIF found for today.")
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

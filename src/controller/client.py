import discord
from discord.ext import commands    

intents = discord.Intents.all()    
bot = commands.Bot(';', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user}')
    

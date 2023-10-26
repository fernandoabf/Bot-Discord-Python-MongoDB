import discord
import datetime
from datetime import timezone
from discord.ext import commands
from src.controller.client import bot
from src.repositories.discord_repository import repository

@bot.command(name = 'avisar')
async def warn(ctx, member:discord.Member):
    
    id = int(ctx.message.content.split()[1])
    reason = ctx.message.content.split()[2:]
    guild = ctx.guild.id
    reason = ' '.join(reason)
    date = datetime.datetime.utcnow() - datetime.timedelta(hours=3)
    date  = date.strftime("%d/%m/%Y ás %H:%M")   
    type = "Aviso"
    author = str(ctx.author.name)
   
    documento = {
        'id': id,
        'reason': reason,
        'type': type,
        'date': date,
        'guild': guild,
        'author': author
    }

    repository.criar_documento(documento)

    if ctx.guild.get_member(id):
        
        warn = discord.Embed()
        warn.title = 'Aviso'

        await member.send(f'{reason}')
    
        

def setup(bot):
    warn(bot)

    
import discord
import datetime
from datetime import timezone
from discord.ext import commands
from src.controller.client import bot
from src.repositories.discord_repository import repository

@bot.command(name = 'ban')
async def ban(ctx, member:discord.Member):
    
    id = int(ctx.message.content.split()[1])
    reason = ctx.message.content.split()[2:]
    guild = ctx.guild.id
    reason = ' '.join(reason)
    date = datetime.datetime.utcnow() - datetime.timedelta(hours=3)
    date  = date.strftime("%d/%m/%Y ás %H:%M")   
    type = "Ban"
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
        
        ban = discord.Embed()
        ban.title = 'Ban'
        await member.send(f'{reason}')
        await member.ban()
        

def setup(bot):
    ban(bot)

    
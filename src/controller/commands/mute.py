import discord
from discord.ext import commands
from src.controller.client import bot
from src.repositories.discord_repository import repository
import datetime

@bot.command(name = 'mutar')
async def mute(ctx, member:discord.Member):
    
    id = int(ctx.message.content.split()[1])
    time = int(ctx.message.content.split()[2])
    reason = ctx.message.content.split()[3:]
    reason = ' '.join(reason)
    guild = ctx.guild.id
    type = "Mute"
    date = datetime.datetime.utcnow() - datetime.timedelta(hours = 3)
    date = date.strftime("%d/%m/%Y ás %H:%M")
    author = str(ctx.author.name)

    timeoutTime = datetime.datetime.utcnow() + datetime.timedelta(hours = time)
    
    if ctx.guild.get_member(id):
        await member.edit(communication_disabled_until= timeoutTime)
        
        documento = {
            'id': id,
            'time': time,
            'type': type,
            'reason': reason,
            'date': date,
            'guild': guild,
            'author': author
        }

        embed = discord.Embed()
        embed.title = "Você foi mutado"
        embed.description = ""

        repository.criar_documento(documento)
        await member.send(reason)


def setup(bot):
    mute(bot)
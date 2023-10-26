import discord
from discord.ext import commands
from src.controller.client import bot
from src.repositories.discord_repository import repository
from bson import ObjectId

@bot.command(name = 'rmvl')
async def removerlog(ctx):

    _id = ctx.message.content.split()[1]
    guild = ctx.guild.id
    filtro = {
        'guild': guild
    } 
    
    filtragem = repository.ler_documentos(filtro)

    if filtragem:
        filtro2 = {
            '_id': ObjectId(_id)
        }
        
        repository.excluir_documento(filtro2)
    
    else:
        print('aaaaa')


def setup(bot):
    removerlog(bot)
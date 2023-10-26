import discord
from discord.ext import commands
from src.controller.client import bot
from src.repositories.discord_repository import repository

@bot.command(name = 'logs')
async def logs(ctx, member:discord.Member):
    
    id = int(ctx.message.content.split()[1])
    guild = ctx.guild.id
    filtro = {
        'id': id,
        'guild': guild
    }
    
    documentos = repository.ler_documentos(filtro)
    
    if documentos:
        embed1 = discord.Embed()
        embed1.title = f'Crimes do id: {id}'
        embed1.color = int(f'00ff00', 16)

        embed2 = discord.Embed()
        embed2.color = int(f'00ff00', 16)
        
        await ctx.channel.send(embed=embed1)

        for documento in documentos:
            if documento['type'] == 'Aviso':
                embed2.title = f"{documento['type']}"
                embed2.description = f"\nMotivo: {documento['reason']}\n\nData de aplicação: {documento['date']}\nID do log: {documento['_id']}"
                await ctx.channel.send(embed=embed2)
            
            elif documento['type'] == 'Mute':
                embed2.title = f"{documento['type']}"
                embed2.description = f"\nMotivo: {documento['reason']}\nTempo de duração: {documento['time']}\n\nData de aplicação: {documento['date']}\nID do log: {documento['_id']}"
                await ctx.channel.send(embed=embed2)
    else: 
        embed3 = discord.Embed()
        embed3.title = 'Usuário está mais limpo que bumbum de neném'
        embed3.color = int(f'ff0000', 16)
        
        return await ctx.channel.send(embed=embed3)

def setup(bot):
    logs(bot)
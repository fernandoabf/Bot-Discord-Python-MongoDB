import discord
from discord.ext import commands    

intents = discord.Intents.all()    
bot = commands.Bot('!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user}')
    
@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel and after.channel.id == 1139391676482342952:
        new_call = await member.guild.create_voice_channel(after.channel.name, category=after.channel.category, user_limit=10, position=1)
        await member.move_to(new_call)
    elif after.channel and after.channel.id == 1139394171921244250:
        new_call = await member.guild.create_voice_channel(after.channel.name, category=after.channel.category, user_limit=5, position=4)
        await member.move_to(new_call)
    if before.channel and (not member.voice or (before.channel.id != after.channel.id)) and len(before.channel.members) == 0 and (before.channel.name == "💻・coding" or before.channel.name == "📞・suporte") and before.channel.id != 1139391676482342952 and before.channel.id != 1139394171921244250:
        await before.channel.delete()
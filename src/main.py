import discord
import os
from src.config.connections import ConfigurationAPIDiscord
from src.controller.client import bot
from discord.ext import commands
from src.repositories.discord_repository import repository

def main():

    for filename in os.listdir('src/controller/commands'):
        if filename.endswith('.py'):
            bot.load_extensions(f'src.controller.commands.{filename[:-3]}')

    bot.run(ConfigurationAPIDiscord.token)
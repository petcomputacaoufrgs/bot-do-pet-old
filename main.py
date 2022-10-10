import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio

# SETUP
load_dotenv()
intent = discord.Intents.all()
bot = commands.Bot(intents=intent, command_prefix=('pet.', 'Pet.', 'PET.'), activity=discord.Activity(type=discord.ActivityType.watching, name="Use pet.help"))
bot.remove_command("help")

# Loading the bot commands
async def load_cogs(bot):
    # COMMANDS
    for file in os.listdir("commands"):
        if file.endswith(".py"):
            cog = file[:-3]
            await bot.load_extension(f'commands.{cog}')

    # EVENTS
    for file in os.listdir("events"):
        if file.endswith(".py"):
            cog = file[:-3]
            await bot.load_extension(f'events.{cog}')

    # HELP
    for file in os.listdir("help"):
        if file.endswith(".py"):
            cog = file[:-3]
            await bot.load_extension(f'help.{cog}')


asyncio.run(load_cogs(bot))

TOKEN = os.getenv("OFFICIAL_TOKEN")

try:
    bot.run(TOKEN)
except:
    os.system("kill 1")
    bot.run(TOKEN)

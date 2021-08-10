import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
bot = commands.Bot(command_prefix="", intents=intents)

@bot.event
async def on_ready():
    print(f"logged in as {bot.user}")

if __name__ == '__main__':

    token = os.getenv('TOKEN')
    bot.run(token)
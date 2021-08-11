import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
bot = commands.Bot(command_prefix="a.", intents=intents)

alphabets = list("abcdefghijklmnopqrstuvwxyz")
chars = []

@bot.event
async def on_ready():
    print(f"logged in as {bot.user}")

@bot.event
async def on_message(ctx):
    global chars

    char = str(ctx.content).lower()

    if len(char) == 1 and char in alphabets:
        chars.append(char)

        if char[len(char)-1] == alphabets[len(chars)-1]:
            await ctx.add_reaction("✅")


        if len(chars) == 26 and chars[len(chars)-1] == "z":
            await ctx.add_reaction("💯")
            await ctx.channel.send(f"Noice !! {ctx.author.mention} Reached The End, There Are No More Letters. Start Again with **a**")
            chars = []

        elif chars[len(chars)-1] != alphabets[len(chars)-1]:
            if len(chars) == 1 and chars[0] != "a":
                chars = []

            else:
                await ctx.channel.send(f"{ctx.author.mention} {alphabets[len(chars)-1]} Comes After {chars[len(chars)-2]} !! Start Again With **a**")
                chars = []
            
            
         


if __name__ == '__main__':

    token = os.getenv('TOKEN')
    bot.run(token)
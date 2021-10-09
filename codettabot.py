#Imports
import discord
from discord.ext import commands
import random 
from dotenv import load_dotenv
import os
#Variables
load_dotenv(os.path.join(os.getcwd(), '.env'))
TOKEN = os.getenv("TOKEN")
PREFIX = os.getenv("PREFIX")
bot = commands.Bot(command_prefix = PREFIX)
token =  TOKEN
x = ["rock","paper","scissor"]

#Bot OnReady Event
@bot.event
def load_extensions():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"cogs.{extension}")
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")
async def on_ready():
    load_extensions()
    print('logged on as')
    print(bot.user.name)
    print(bot.user.id)
    print('---------')
   

class challenge(commands.Cogs):
  def __init__(self,bot):
    self.bot = bot  

@bot.command()
async def baaa(ctx):
    await ctx.send("baaa wassup baaa") 

@bot.command()
async def hand(ctx):
    await ctx.send("raised") 

@bot.command()
async def offline(ctx):
    await ctx.send("ok I'm sleepy now, get out") 

@bot.command()
async def myname(ctx, Lilia):
  await ctx.send("Your name is: " + Lilia)

@bot.command("add")
async def addition(ctx, eqn1 : int, eqn2 : int):
 sumofeq = eqn1 + eqn2
 print(sumofeq)
 await ctx.send(sumofeq)

@bot.command("creator") 
async def creator(ctx):
  message = ctx.Union
  print(message)
  await ctx.send(message) 

@bot.command()
async def rps(ctx, x):
   bot_choice = random.choice(["rock","paper","scissors"])
   await ctx.send(bot_choice)

   if x == "rock" and bot_choice == "rock":
     await ctx.send("TIED! lets not play fire with fire")

   if x == "rock" and bot_choice == "paper":
     await ctx.send("You Lose :)) ya can't beat meeee")

   if x == "rock" and bot_choice == "scissors":
     await ctx.send("You WIN! but I'll get you next time...")



bot.run(token)
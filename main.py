import discord
import requests

from discord.ext import commands

bot = commands.Bot(command_prefix= "-", intents=discord.Intents.all())

@bot.event
async def on_listo():
    print(f"Soy {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("pong!")



@bot.command()
async def buscar(ctx):
    url= ctx 
    respuesta = requests.get(url)

    print (respuesta)



bot.run("MTIxMjgyMzE1MDAyMzI4NjgyNA.GPSgUb.y_agewj14vozgLW9QqG0T7j1_J8urI6QuHvhHo")
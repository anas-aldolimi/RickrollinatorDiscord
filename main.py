import discord
import os
import time
from discord.ext import commands
from keep_alive import keep_alive

bot = commands.Bot(command_prefix="-")

song = open('never.txt')


@bot.event
async def on_ready():
    print("done")


@bot.command
@bot.event
async def on_message(ctx):
    role = discord.utils.get(ctx.guild.roles, name="rickroller")
    if role in ctx.author.roles and ctx.content.startswith('-r'):
        song = open('never.txt')
        for line in song:
            await ctx.channel.send(line)
            time.sleep(1)
        song.close()
    elif ctx.content.startswith('-r'):
        await ctx.channel.send("you don't have the 'rickroller' role")
    else:
        ctx.channel.send('there was an error')


keep_alive()
bot.run(os.getenv('token'))

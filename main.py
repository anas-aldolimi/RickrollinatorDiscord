import discord
import os
from asyncio import sleep

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


ffmpeg_executable_path = "path/to/ffmpeg"

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
        
    if message.content.startswith('$VC'):
        Voicechannel = message.author.voice.channel
        vc = await Voicechannel.connect()
        src = discord.FFmpegPCMAudio(executable=ffmpeg_executable_path, source="./GOSPEL.mp3")
        vc.play(src)
        while vc.is_playing():
            await sleep(1)
        await vc.disconnect()
        
        
        


    if message.content.startswith('$DoTheThing'):
        with open("Never.txt", 'r') as file:
        # Read the lines of the file
            file_lines = file.readlines()
 
            # Print each line
        print("File Content:")
        for line in file_lines:
            await sleep(1)
            await message.channel.send(line.strip())
        

client.run('discord/app/token/here')
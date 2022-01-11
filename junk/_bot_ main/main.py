from discord import FFmpegPCMAudio
from discord.ext import commands
from discord.utils import get
import json

with open("config.json") as file:
    config = json.load(file)

bot = commands.Bot(command_prefix='/', description='A simple Discord bot')

@bot.command(
    name="test",
    description="This is just a test command."
)
async def hello(ctx):
    await ctx.send("Test post, please ignore.")

async def join(ctx, voice):
    channel = ctx.author.voice.channel

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect() 

@bot.command()
async def play(ctx, *, query):
    #Solves a problem I'll explain later
    FFMPEG_OPTS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    video, source = search(query)
    voice = get(bot.voice_clients, guild=ctx.guild)

    await join(ctx, voice)
    await ctx.send(f'Now playing {info['title']}.')

    voice.play(FFmpegPCMAudio(source, **FFMPEG_OPTS), after=lambda e: print('done', e))
    voice.is_playing()

bot.run(config["DISCORD_TOKEN"])

import discord
from discord.ext import commands
from discord import guild
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
import json 
from flask import Flask, redirect, request
import startup
from multiprocessing import Process

app = Flask("virtual speaker")



@app.route('/')
def index():
    response = startup.getUser()
    return redirect(response)

@app.route('/callback/')
def callback():
    startup.getUserToken(request.args['code'])

    return redirect("http://localhost:3000")

with open("config.json", 'r') as file:
    config = json.load(file)

guild_ids = [688477783999119410]

client = commands.Bot(command_prefix="!")
slash = SlashCommand(client, sync_commands=True)

@slash.slash(
    name="hello",
    description="Just sends a message",
    guild_ids= guild_ids
    )
async def _hello(ctx:SlashContext):
    await ctx.send("World!")

@slash.slash(
    name="Authenticate",
    description="Authenticate a WebPlay Instance",
    guild_ids= guild_ids
)
async def _authenticate(ctx:SlashContext):
    authURL = startup.getUser()
    await ctx.author.send("Click here to login: [login]("+ authURL+")")


@slash.slash(
    name="Play",
    description="Resumes music in your voice channel",
    guild_ids= guild_ids
)
async def _connect(ctx:SlashContext):
    await ctx.send("Connecting!")

@slash.slash(
    name="Join",
    description="Joins your current voice channel",
    guild_ids= guild_ids
)
async def _join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@slash.slash(
    name="Leave",
    description="Leaves the current voice channel",
    guild_ids= guild_ids
)
async def _leave(ctx):
    await ctx.voice_client.disconnect()

def discordRunner():
    print("Starting discord bot")
    client.run(config["DISCORD_TOKEN"])
    print("made a discord bot")

def flaskRunner():
    print("Starting Flask")
    app.run(host='0.0.0.0')
    print ("flask webserver is running")


def main():
    dp = Process(target=discordRunner)
    fp = Process(target=flaskRunner)
    dp.start()
    fp.start()

if __name__ == "__main__":
    main()

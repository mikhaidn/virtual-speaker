import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
import json 

with open("config.json") as file:
    config = json.load(file)

client = commands.Bot(command_prefix="!")
slash = SlashCommand(client, sync_commands=True)

@slash.slash(
    name="hello",
    description="Just sends a message",
    guild_ids=[759158765483196428]
)
async def _hello(ctx:SlashContext):
    await ctx.send("World!")

client.run(config["DISCORD_TOKEN"])

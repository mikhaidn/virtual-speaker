from discord.ext import commands
import json

with open("config.json") as file:
    config = json.load(file)

bot = commands.Bot(command_prefix='..', description='A simple Discord bot')

@bot.command(
    name="test",
    description="This is just a test command."
)
async def hello(ctx):
    await ctx.send("Test post, please ignore.")

bot.run(config["DISCORD_TOKEN"])

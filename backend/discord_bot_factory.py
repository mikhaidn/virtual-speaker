import discord
from discord.ext import commands
from discord import guild
from discord_slash import SlashCommand, SlashContext, cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option
import json
from spotify_cog import SpotifyCog

class DiscordBotRunner:
    def __init__(self, bot, slash, token):
        self.bot = bot
        self.slash = slash
        self.token = token

    def run(self):
        self.bot.run(self.token)

class DiscordBotRunnerFactory:
    __token = None
    __guild_ids = None

    
    def create(spotifyAuthenticator):
        with open("config.json", 'r') as file:
            config = json.load(file)
            token = config["DISCORD_TOKEN"]
            guild_ids = config["GUILD_IDS"]

        bot = commands.Bot(command_prefix="!")
        slash = SlashCommand(bot, sync_commands=True)

        bot.add_cog(SpotifyCog(bot,guild_ids,spotifyAuthenticator))
        return DiscordBotRunner(bot,slash,token)





    






import discord
from discord.ext import commands
from discord import guild
from discord_slash import SlashCommand, SlashContext, cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option
from spotify_auth import SpotifyAuthenticator
import json

class SpotifyCog(commands.Cog):
    def __init__(self, bot, guild_ids, spotifyAuthenticator):
        self.bot = bot
        self._whitelisted_guilds = guild_ids
        self._last_member = None
        self.authenticator = spotifyAuthenticator


    @commands.command()
    async def ping(self, ctx):
            print("got here")
            await ctx.send('Pong!')  

    @commands.command()
    async def login(self, ctx):

        authURL = self.authenticator.buildAuthCall()
        content = authURL

        embedVar = discord.Embed(title="Login to Spotify", description="[Click here to give the bot permissions to stream spotify](<"+authURL+">)", color=0x72d345)

        await ctx.author.send(embed=embedVar)

    @commands.command()
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()

    @commands.command()
    async def leave(self,ctx):
        await ctx.voice_client.disconnect()
    # -----------------

#     @cog_ext.cog_slash(
#         name="Ping",
#         description="ping")
#     async def _ping(self, ctx: SlashContext):
#         print("got here")
#         await ctx.send('Pong!')   

#     @cog_ext.cog_slash(
#         name="Login",
#         description="Login to Spotify")
#     async def _login(self, ctx: SlashContext):

#         authURL = self.authenticator.buildAuthCall()
#         content = authURL
  
#         await ctx.author.send(content)

#     @cog_ext.cog_slash(
#         name="Join",
#         description="Joins your current voice channel"
#    )
#     async def _join_channel(self, ctx: SlashContext):
#         channel = ctx.author.voice.channel
#         await channel.connect()

#     @cog_ext.cog_slash(
#         name="Leave",
#         description="Leaves the current voice channel",
#     )
#     async def _leave_channel(self,ctx: SlashContext):
#         await ctx.voice_client.disconnect()

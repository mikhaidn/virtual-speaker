import json
from flask import Flask, redirect, request, send_from_directory 
from multiprocessing import Process 
from discord_bot_factory import DiscordBotRunnerFactory 
from spotify_auth import SpotifyAuthenticator 
from spotify_cog import SpotifyCog   
app = Flask("virtual speaker")       
#Port and callback url can be changed or left to localhost:5000 
port =  "5000" 
callback_url = "http://localhost" 
redirect_uri = "{}:{}/callback/".format(callback_url, port) 
spotify = SpotifyAuthenticator(redirect_uri)

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

@app.route('/auth/login')
def index():
    response = spotify.buildAuthCall()
    return redirect(response)

@app.route('/callback/')
def callback():
    print ("got here")
    token = spotify.getToken(request.args['code'])
    return str(token)


def discordRunner():
    print("Starting discord bot")
    runner = DiscordBotRunnerFactory.create(spotify)
    runner.run()
    

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

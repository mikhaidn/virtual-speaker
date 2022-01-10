from flask import Flask, redirect, request
import startup

@app.route('/')
def index():
    response = startup.getUser()
    return redirect(response)
                                                                
@app.route('/callback/')
    startup.getUserToken(request.args['code'])

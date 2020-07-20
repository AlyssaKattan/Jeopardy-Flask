from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect
import random
import model

import requests #To access our API

# -- Initialization section --
app = Flask(__name__)

## secret key for session (In production, you would set this key via an environment variable)
app.secret_key = b'HO\xf8\xff+\n\x1e\\~/;}'

@app.route('/')
@app.route('/index')
def index():
    session["name"] = "Alyssa"
    session["score"] = 0
    return render_template('index.html')

@app.route('/random')
def jeopardy_random():
    API_endpoint= "https://jservice.io/api/random" #identify what endpoint (url) is
    r= requests.get(API_endpoint) #computer visits url and stores output as a response object
    data= r.json() #stores rest of misc. data
    clue= data[0]
    session["clue"]= clue #session variable travels btwn py & html, "clue" name is up to u
    return render_template('clue.html') 
    
@app.route('/results', methods = ['GET', 'POST'])
def handle_results():
    if request.method == 'GET':
        return redirect("/random") #redirect user back to start page
    else:
        form = request.form #intake answer
        session['form']= form #remember form 
        answer = form['answer']
        points = model.calc_points(session["clue"], answer)
        session['score'] += points
        return render_template('results.html')
    
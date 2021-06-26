from flask import Flask
from flask import render_template
import json 

app=Flask(__name__)

@app.route('/')
def index():
    f = open('new.json')
    raw = f.read()
    data = json.load(raw)
    return render_template('lista.html', news=data )

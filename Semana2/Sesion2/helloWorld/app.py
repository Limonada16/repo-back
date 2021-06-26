from flask import Flask
from flask.globals import request
from flask.templating import render_template
 
app = Flask(__name__)
@app.route('/')
def index():
    noticias =[
        "Debate del domingo 23 de mayor"
        "¿Como saber si tengo multas electorales?"
        "El revelador informe que el pentagono alista sobre todo lo que sabe EE.UU"
    ]
    name = request.args.get("name")
    return render_template("index.html", title="Titulo", name=name, news=noticias)

from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template
import json
from utils import collections
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    raw = open('../../Semana2/Sesion3/data/products.json')
    products = json.load(raw)

    product_types = collections.unique_keys(products, "type")

    return render_template("index.html", products=products)
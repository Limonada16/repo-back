#from api.categoria_api import CategoriaAPI

from flask import Flask
from flask_mysqldb import MySQL
from flask_restful import Resource, Api

app = Flask(__name__)
mysql = MySQL(app)
api = Api(app)

from api.categoria_api import CategoriaAPI
from api.post import Post
from api.hello_api import HelloWorld
from api.producto_categoria import PorductoCat

app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "myblog"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

api.add_resource(HelloWorld, '/hello')
api.add_resource(CategoriaAPI, '/categoria')
api.add_resource(Post, '/post')
api.add_resource(PorductoCat, '/post/<id>/productos')
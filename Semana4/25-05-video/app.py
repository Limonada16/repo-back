from sqlalchemy import engine
from user import User
from flask import Flask
from flask import request   
from flask import jsonify
import db 

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

@app.route('/users', methods=['POST'])
def create_user():
    
    session = db.Session()
    #CREAR UN USUARIO
    user = request.json

    #CREAR NUEVA INSTANCIADE MODELO USER
    new_user = User()
    new_user.nombre = user["nombre"]
    new_user.apellido = user["apellido"]
    new_user.dni = user["dni"]
    new_user.telefono = user["telefono"]
    new_user.correo = user["correo"]

    session.add(new_user)
    session.commit()
    return "Ok", 201
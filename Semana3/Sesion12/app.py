from sqlalchemy import engine
from user import User
from flask import Flask
from flask import request
from flask import jsonify
import db

app = Flask(__name__)

@app.route('/')

def index():
    return "Hello"

# RUTA QUE UTILIZA EL METODO POST PARA CREAR CONTENIDO
@app.route('/users', methods=['POST'])

def create_users():

    # CREACIÓN DE UNA SESIÓN    
    session = db.Session()

    #CREAR UN USUARIO
    user = request.json #request.json convierte el string en un json

    # CREAR NUEVA INSTANACIA DE MODELO USER
    new_user = User()
    new_user.nombre = user["nombre"]
    new_user.apellido = user["apellido"]
    new_user.dni = user["dni"]
    new_user.telefono = user["telefono"]
    new_user.correo = user["correo"]

    session.add(new_user)
    session.commit()
    return "OK", 201    


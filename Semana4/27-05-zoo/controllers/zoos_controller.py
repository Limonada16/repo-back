from flask_restful import Resource
from sqlalchemy.orm import session
from ..models.zoo import Zoo
from ..database import Session
from flask import request, jsonify
from sqlalchemy.sql.expression import select

class ZoosController(Resource):
    #LISTAR ZOOLOGICOS
    def get(self):
        zoos = select(Zoo)
        return jsonify(zoos)

    #CREAR ZOOLOGICOS
    def post(self):
        session = Session()

        #PAYLOAD
        data = request.json

        zoo = Zoo()
        zoo.nombre = data ["nombre"]
        zoo.ciudad = data ["ciudad"]
        zoo.tamano = data ["tamano"]
        zoo.presupuesto_anual = data ["presupuesto_anual"]

        session.add(zoo)
        session.commit()
        
        return 'Ok', 201    
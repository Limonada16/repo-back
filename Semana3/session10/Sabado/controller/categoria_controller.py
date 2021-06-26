from Models.categoria import CategoriaModel
from flask_restful import Resource
from flask import jsonify
from app import mysql

class CategoriaController(Resource):
    def get(self):
        categorias = CategoriaModel()
        return jsonify(categorias.all())

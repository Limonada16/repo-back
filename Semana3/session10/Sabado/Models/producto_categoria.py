from flask_restful import Resource
from app import mysql
from flask import jsonify
class PorductoCat(Resource):
    def get(self, id):
        cur = mysql.connection.cursor()
        cur.execute('''
            SELECT p.titulo, c.nombre FROM post AS p
            INNER JOIN usuario as u
            on p.idUsuario = u.idUsuario
            INNER JOIN categoria as c
            ON p.idCategoria = ''' + id)
        result = cur.fetchall()
        return jsonify(result)

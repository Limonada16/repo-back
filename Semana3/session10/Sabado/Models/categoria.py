from flask_restful import Resource
from app import mysql
from flask import jsonify

class CategoriaModel():
    def all(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM post")
        return cur.fetchall()

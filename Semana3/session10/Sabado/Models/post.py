from flask_restful import Resource
from app import mysql
from flask import jsonify

class Post(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM post")
        result = cur.fetchall()
        return jsonify(result)

from flask_restful import Resource


from flask_restful import Resource

class HelloController(Resource):
    def get(self):
        return "Hello World"

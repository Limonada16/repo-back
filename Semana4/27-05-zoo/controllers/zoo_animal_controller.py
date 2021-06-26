from flask_restful import Resource

class ZooAnimalController(Resource):
    def get(self, zoo_id, animal_id):
        pass
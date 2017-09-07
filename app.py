from flask import Flask, jsonify
from flask_restful import request, Api, Resource
from flask_pymongo import PyMongo

from model.model import carModel

app = Flask(__name__)
api = Api(app)
mongo = PyMongo(app)

cars = {
    {
        'id': '001',
        'make': 'Tesla',
        'model': 'Model S',
        'colour': 'White'
    },

    {
        'id': '002',
        'make': 'BMW',
        'model': 'i8',
        'colour': 'Orange'
    },

    {
        'id': '003',
        'make': 'Tesla',
        'model': 'Model X',
        'colour': 'Grey'
    }
}

class User(Resource):
    @staticmethod
    def get(car_id):

        cars = carModel.find_by_id(car_id)
        data = jsonify(cars.__dict__)
        data.status_code = 200
        return data

    @staticmethod
    def post():

        payload = request.get_json()



        data = jsonify(cars.__dict__)
        data.status_code = 201

        return data


api.add_resource(cars, '/<car_id>')
api.add_resource(cars, '/')


if __name__ == '__main__':
    app.run(debug=True)
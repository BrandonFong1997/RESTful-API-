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
        'Make': 'Tesla',
        'Model': 'Model S',
        'Colour': 'White'
    },

    {
        'id': '002',
        'Make': 'BMW',
        'Model': 'i8',
        'Colour': 'Orange'
    },

    {
        'id': '003',
        'Make': 'Tesla',
        'Model': 'Model X',
        'Colour': 'Grey'
    }
}

class User(Resource):
    @staticmethod
    def get(car_id):

        cars = carModel.find_by_id(car_id)
        data = jsonify(cars.__dict__)
        data.status_code = 200
        return data

api.add_resource(cars, '/<car_id>')


if __name__ == '__main__':
    app.run(debug=True)
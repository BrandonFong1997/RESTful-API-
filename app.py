from flask import Flask, jsonify
from flask_restful import request, Api, Resource
from flask_pymongo import PyMongo

from model.model import carModel

app = Flask(__name__)
api = Api(app)
mongo = PyMongo(app)

class Car(Resource):

    def get(self, car_id):

        cars = carModel.find_by_id(car_id)
        data = jsonify(cars.__dict__)
        data.status_code = 200
        return data

    def put(self, car_id):

        payload = request.get_json()

        cars = carModel.update_car(car_id, payload)

        data = jsonify(cars.__dict__)
        data.status_code = 200

        return data

    def delete(self, car_id):

        response = carModel.delete_car(car_id)

        data = jsonify(response)
        data.status_code = 200

        return data

class CarQuery(Resource):

    def post(self):

        payload = request.get_json()

        cars = carModel.create_car(payload)

        data = jsonify(cars.__dict__)
        data.status_code = 201

        return data

    def get(self):

        query_cars = [car.__dict__ for car in carModel.get_all_cars()]

        data = jsonify(query_cars)
        data.status_code = 200

        return query_cars


api.add_resource(Car, '/<car_id>')
api.add_resource(CarQuery, '/')


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=5000)

    # DOCKER TEST host = '0.0.0.0'
    # LOCAL TEST host = '127.0.0.1'

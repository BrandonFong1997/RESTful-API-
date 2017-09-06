from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

cars = {
    'Tesla':{
        'Model_S': 'Grey',
        'Model_X': 'Red',
        'Model_3': 'White'
    },

    'BMW':{
        'i8': 'Orange',
        'x5': 'Black'
    }
}

parser = reqparse.RequestParser()
parser.add_argument('car')

class Model(Resource):
    def get(self, company, model):
        return cars[company][model]

class Company(Resource):
    def get(self, company):
        return cars[company]

class Cars(Resource) :
    def get(self):
        return cars

api.add_resource(Cars, '/cars')
api.add_resource(Company, '/cars/<company>')
api.add_resource(Model, '/cars/<company>/<model>')

if __name__ == '__main__':
    app.run(debug=True)

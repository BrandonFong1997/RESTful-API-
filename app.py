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
parser.add_argument('Company')
parser.add_argument('Model')
parser.add_argument('Colour')

class Model(Resource):
    def get(self, company, model):
        return cars[company][model]

class Company(Resource):
    def get(self, company):
        return cars[company]

    def put(self, company):
        args = parser.parse_args()
        model = {args['Model']:args['Colour']}
        cars[company] = model
        return model, 200

    def delete(self, company):
        del cars[company]
        return '', 204

class Cars(Resource) :
    def get(self):
        return cars

    def post(self):
        args = parser.parse_args()
        cars[args['Company']][args['Model']] = args['Colour']
        return {args['Model']:args['Colour']}, 200

api.add_resource(Cars, '/cars')
api.add_resource(Company, '/cars/<company>')
api.add_resource(Model, '/cars/<company>/<model>')

if __name__ == '__main__':
    app.run(debug=True)
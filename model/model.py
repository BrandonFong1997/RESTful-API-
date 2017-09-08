from model.dao import carDao

class carModel:
    def __init__(self, collection):
        self.id = str(collection['_id'])
        self.make = collection['make']
        self.model = collection['model']
        self.colour = collection['colour']

    @staticmethod
    def find_by_id(car_id):
        dao = carDao()
        cars = dao.get_car_by_id(car_id)

        car_model = carModel(cars)

        return car_model

    @staticmethod
    def create_car(payload):
        dao = carDao()

        cars = dao.create_car(payload)
        car_model = carModel(cars)

        return car_model

    @staticmethod
    def update_car(car_id, payload):
        dao = carDao()

        cars = dao.update_car(car_id, payload)

        car_model = carModel(cars)

        return car_model

    @staticmethod
    def delete_car(car_id):
        dao = carDao()

        response = dao.delete_car(car_id)

        if response:
            response = {'message': 'car deleted'}

        return response

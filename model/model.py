from model.dao import carDao

class carModel:
    def __init__(self, collection):
        self.id = collection['_id']
        self.make = collection['make']
        self.model = collection['model']
        self.colour = collection['collection']

    @staticmethod
    def find_by_id(car_id):
        dao = carDao()
        cars = dao.get_car_by_id(car_id)
        car_model = carModel(cars)

        return car_model

    @staticmethod
    def create_car(payload):




from model.dao import carDao

class carModel:
    def __init__(self, collection):
        self.id = str(collection['_id']) if '_id' in collection else None
        self.make = collection['make'] if 'make' in collection else None
        self.model = collection['model'] if 'model' in collection else None
        self.colour = collection['colour'] if 'colour' in collection else None

    def find_by_id(car_id):
        dao = carDao()
        cars = dao.get_car_by_id(car_id)

        car_model = carModel(cars) if cars else None

        return car_model

    def create_car(payload):
        dao = carDao()

        cars = dao.create_car(payload)
        car_model = carModel(cars)

        return car_model

    def update_car(car_id, payload):
        dao = carDao()

        cars = dao.update_car(car_id, payload)

        car_model = carModel(cars) if cars else None

        return car_model

    def delete_car(car_id):
        dao = carDao()

        cars = dao.delete_car(car_id)

        if cars:
            cars = {'message': 'car deleted'}

        return cars

    def get_all_cars():
        dao = carDao()

        cars = []
        retrieve = dao.get_all_cars()

        for total_cars in retrieve:
            cars.append(carModel(total_cars))

        return cars

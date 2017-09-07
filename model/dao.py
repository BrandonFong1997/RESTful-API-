from mongo_utils import MongoUtils
from pymongo.database import ObjectId

class carDao:
    def __init__(self):
        print self._logger

    def get_connection(self):
        collection = "carList"

        connection = MongoUtils.get_mongo_connection()
        db = getattr(connection, collection)

        return db

    def get_user_by_id(self, car_id):
        _car_user = None

        car_db = self.get_connection()
        car_cursor = car_db.find({"_id": ObjectId(car_id)})
        for car in car_cursor:
            _car_user = car

        return _car_user

    def create_car(self, cars):
        car_db = self.get_connection()

        _car_user = car_db.find_one({"_id": int(cars['_id'])})
        if _car_user:
            return None

        result = car_db.insert_one(cars)
        _new_car = car_db.find_one({"_id": result.inserted_id})

        return _new_car

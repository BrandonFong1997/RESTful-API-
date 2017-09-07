from mongo_utils import MongoUtils
from pymongo.database import ObjectId

class carDao:
    def __init__(self):
        self._logger = print

    def get_collection(self):
        collection_name = "carList"

        db = MongoUtils.get_mongo_connection_db()
        collection = db[collection_name]

        return collection

    def get_car_by_id(self, car_id):

        car_collection = self.get_collection()
        _car_user = car_collection.find_one({"_id": ObjectId(car_id)})
        return _car_user

    def create_car(self, cars):
        car_db = self.get_collection()

        _car_user = car_db.find_one({"_id": int(cars['_id'])})
        if _car_user:
            return None

        result = car_db.insert_one(cars)
        _new_car = car_db.find_one({"_id": result.inserted_id})

        return _new_car

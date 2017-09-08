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
        car_collection = self.get_collection()

        result = car_collection.insert_one(cars)
        _new_car = car_collection.find_one({"_id": result.inserted_id})

        return _new_car

    def update_car(self, car_id, cars):
        car_db = self.get_collection()

        result = car_db.update_one({"_id": ObjectId(car_id)}, {"$set": cars})

        _car_user = car_db.find_one({"_id": ObjectId(car_id)})

        return _car_user

    def delete_car(self, car_id):
        car_db = self.get_collection()

        _car_user = car_db.find_one({"_id": ObjectId(car_id)})
        if not _car_user:
            return None

        delete_result = car_db.delete_one({"_id": ObjectId(car_id)})

        return delete_result

from mongo_utils import MongoUtils
from pymongo.database import ObjectId

class carDao:
    def __init__(self):
        self._logger = print

    def get_connection(self):
        collection = config.MONGO_DBNAME

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


from pymongo import MongoClient

class MongoUtils:
    def __init__(self):
        pass

    @staticmethod
    def get_mongo_connection():

        client = MongoClient(host)

        db = getattr(client)

        return db
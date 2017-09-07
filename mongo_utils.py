from pymongo import MongoClient

class MongoUtils:
    def __init__(self):
        pass

    @staticmethod
    def get_mongo_connection():

        host = "http://127.0.0.1:27017"
        table = "cars"

        client = MongoClient(host)

        db = getattr(client, table)

        return db
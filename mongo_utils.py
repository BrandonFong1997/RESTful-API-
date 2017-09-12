from pymongo import MongoClient

class MongoUtils:
    def __init__(self):
        pass

    @staticmethod
    def get_mongo_connection_db():

        host = "mongo"
        # DOCKER TEST host = "mongo"
        # LOCAL TEST host = "mongodb://127.0.0.1:27017"
        table = "cars"

        client = MongoClient(host)

        db = getattr(client, table)

        return db

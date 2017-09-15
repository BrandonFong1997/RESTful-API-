from pymongo import MongoClient

import util.config.settings as config


class MongoUtils:
    def __init__(self):
        pass

    @staticmethod
    def get_mongo_connection_db():

        host = config.MONGO_HOST
        # host = "mongodb://127.0.0.1:27017"

        # DOCKER TEST host = "mongo"
        # LOCAL TEST host = "mongodb://127.0.0.1:27017"

        table = config.MONGO_COLLECTION

        client = MongoClient(host)

        db = getattr(client, table)

        return db

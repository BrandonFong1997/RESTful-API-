import os

MONGO_HOST = os.environ['MONGO_HOST'] if 'MONGO_HOST' in os.environ else None
MONGO_DBNAME = os.environ['MONGO_DBNAME'] if 'MONGO_DBNAME' in os.environ else None

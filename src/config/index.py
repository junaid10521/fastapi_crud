from pymongo import MongoClient
import os
import certifi

MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = int(os.getenv("MONGO_PORT"))
MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_DATABASE = os.getenv("MONGO_DATABASE")
MONGO_ATLAS_URL = os.getenv("MONGO_ATLAS_URL")


class MongoConfig:
    def __init__(self):
        if MONGO_ATLAS_URL:
            self.client = MongoClient(MONGO_ATLAS_URL, tlsCAFile=certifi.where())
        else:
            self.client = MongoClient(
                MONGO_HOST, MONGO_PORT, username=MONGO_USERNAME, password=MONGO_PASSWORD
            )
        self.db = self.client[MONGO_DATABASE]


mongo_config = MongoConfig()

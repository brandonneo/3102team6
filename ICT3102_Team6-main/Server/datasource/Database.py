import pymongo
from pymongo import ssl_support
import os

class Database:
    client = pymongo.MongoClient(os.environ["MONGOSCONNECTIONSTRING"])
    # client = pymongo.MongoClient("mongodb://localhost:27017")

    db = client["ICT3102"]
    
    
import pymongo
from pymongo import ssl_support

class Database:
    client = pymongo.MongoClient("mongodb://172.17.0.1:27017")
    db = client["ICT3102"]
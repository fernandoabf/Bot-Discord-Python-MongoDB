import pymongo
from pymongo import MongoClient
from src.config.connections import ConfigurationDB

class ConnectionMongo:
   
    client = pymongo.MongoClient(ConfigurationDB.connection_string)
    db = client['Fone']
    collection = db['Bluetooth']

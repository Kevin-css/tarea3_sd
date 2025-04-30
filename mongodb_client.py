from pymongo import MongoClient
import os

def conectar_mongo():
    mongo_url = os.getenv("MONGO_URL", "mongodb://localhost:27017")
    cliente = MongoClient(mongo_url)
    db = cliente["sistema_sd"]
    return db
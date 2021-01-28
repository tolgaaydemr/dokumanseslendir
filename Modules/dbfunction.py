from pymongo import MongoClient
import random


def functionFind(collection_name):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["nlp"]
    collection = db[collection_name]
    num = random.randrange(0, 3)
    # FIND METOD CALISTIRMA
    for w in collection.find({}):
        x = w["answer"][num]
    return x

from pymongo import MongoClient
from dotenv import load_dotenv
import os


def startmongo():
    global client
    global db
    global collection
    load_dotenv()
    mongo_uri = os.getenv("MONGO_URI")
    client = MongoClient(mongo_uri)
    db = client["todos"]
    collection = db["todos"]
    print("connected to MongoDB")
    


'''load_dotenv()
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)

db = client["todos"]

collection = db["todos"]

print("Connected to MongoDB")'''


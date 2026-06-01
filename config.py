from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))

collection = None

def startmongo():
    global client
    global db
    global collection

    mongo_uri = os.getenv("MONGO_URI")

    client = MongoClient(mongo_uri)

    db = client["todos"]

    collection = db["todos"]

    print("connected to MongoDB")
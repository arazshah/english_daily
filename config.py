import os
from pymongo import MongoClient


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    MONGO_URI = os.environ.get(
        'MONGO_URI') or 'mongodb://localhost:27017/myflaskapp'


# Initialize MongoDB client
client = MongoClient(Config.MONGO_URI)
db = client.myflaskapp

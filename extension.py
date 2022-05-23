from flask_pymongo import PyMongo
from pymongo import MongoClient

client=MongoClient('mongodb://localhost:27017/')
db=client.criminal_records
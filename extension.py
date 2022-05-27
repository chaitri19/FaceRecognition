#Importing pymongo library to connect to mongodb database.
from pymongo import MongoClient

#Connecting to mongodb database at localhost 27017
client=MongoClient('mongodb://localhost:27017/')
#We have created a database named criminal_records.
db=client.criminal_records
#In criminal_records we have created a collection named Criminal.
mycol=db['Criminal']
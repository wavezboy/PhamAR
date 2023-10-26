import pymongo

import pymongo

# MongoDB connection setup
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["pham"]  # Replace with your MongoDB database name
collection = db["users"]





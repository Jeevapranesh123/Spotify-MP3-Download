
import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Spotify"]
col = db["Songs"]

data = col.find()

final  = []

for i in data:
    for j in i['list']:
        final.append(j)

col.insert_one({"id":2,"list":final})
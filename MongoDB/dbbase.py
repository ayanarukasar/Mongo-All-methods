import pymongo

class DBBase():
    def __init__(self, mongourl):
        self.client = pymongo.MongoClient(mongourl)

    def getDB(self, dbname):
        return self.client[dbname]

    def my_insert_one(self, collobj, data):
        collobj.insert_one(data)

    def my_insert_many(self, collobj, datalist):
        collobj.insert_many(datalist)



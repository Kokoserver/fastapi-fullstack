from pymongo import MongoClient
from server.setting import database_url
from server import mixin






class Database(object):
    __DATABASE = None


    @staticmethod
    def connectDb():
        __client = MongoClient(database_url)
        Database.__DATABASE = __client["ennibee"]



    @staticmethod
    def save(collection:str, data:dict):
       return Database.__DATABASE[collection].insert_one(data)
        
        

    @staticmethod
    def get(collection:str, data:dict):
        data = Database.__DATABASE[collection].find(data)
        return mixin.getData(data, mode=False)


    @staticmethod
    def delete(collection:str, data:dict):
        return Database.__DATABASE[collection].delete_one(data)
       


    @staticmethod
    def update(collection:str, new_data:dict, old_data:dict):
         data = Database.__DATABASE[collection].update(old_data, {"$set":new_data})
         return mixin.getData(data, mode=False)
       


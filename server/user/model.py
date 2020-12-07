
from server.db import Database
from uuid import uuid4
from datetime import datetime
from server.mixin import databaseconnect



class UserModel (object):
    __collection = "account"
    databaseconnect()

    def __init__(self, firstname:str, lastname:str, email:str, password:str, phone:str):   
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.password = password


    def json(self):
        return {
            "_id":uuid4().hex,
            "firstname":self.firstname,
            "lastname":self.lastname,
            "email":self.email,
            "phone":self.phone,
            "password":self.password,
            "active":False,
            "admin":False,
            "created_at":datetime.today(),
            }


    def save(self):
        return Database.save(UserModel.__collection, data= self.json())

    @staticmethod
    def get_user(data):
        return (Database.get(UserModel.__collection, data))

    @staticmethod
    def all_user():
        return Database.get(collection=UserModel.__collection, data={})

    @staticmethod
    def remove_user(data:dict):
        return Database.delete(UserModel.__collection, data=data)

    @staticmethod
    def update_user(olddata, newdata):
        return Database.update(UserModel.__collection, new_data=newdata, old_data=olddata)

   
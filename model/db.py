#from pymongo import MongoClient
from mongoengine import *


def create_db_connection(db_name:str, host:str = 'localhost', port:int = 27017):
    connect(db_name, host=host, port=port)


class UserDb(Document):
    chat_id  = IntField(unique=True)
    username = StringField()
    password = StringField()




#def create_connection(host:str = 'localhost', port:int = 27017):
    
#    client = MongoClient(host, port)
#    return client

from pymongo import MongoClient

def create_connection(host:str = 'localhost', port:int = 27017):
    
    client = MongoClient(host, port)
    return client

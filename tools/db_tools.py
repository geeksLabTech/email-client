import pymongo

def search_user(identifier, table):
    return table.find({'identifier': identifier})
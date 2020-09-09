import pymongo

def search_user(identifier, table):
    return table.search_one({'identifier': identifier})
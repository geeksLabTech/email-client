import json

def read_config(path:str):
    config = {}
    with open(path, 'r') as json_file:
        config = json.load(json_file)
    
    return config
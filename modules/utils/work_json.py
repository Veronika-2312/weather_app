import json
import os

def read_json(file_name:str):
    path = os.path.abspath(os.path.join(__file__, "..", "..", "..","json", file_name))
    with open(path, mode = "r") as file:
        data = json.load(file)
        return data
def write_json(file_name:str, data:dict):
    path = os.path.abspath(os.path.join(__file__, "..", "..", "..","json", file_name))
    with open(path, mode = "w") as file:
        json.dump(data, file, indent = 4, ensure_ascii = False)

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

url = "mongodb+srv://Darkilling:H3r0g4m3rs@clusterluis.hquplkv.mongodb.net/?retryWrites=true&w=majority&appName=clusterluis"

def conexion ():
    cliente = MongoClient(url, server_api = ServerApi('1'))

    try:
        cliente.admin.command('ping')
        db = cliente.evaluacion2
        print("conectado a MongoDB")
        return (db)
    except Exception as e:
        print(e)

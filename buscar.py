from bson import json_util, ObjectId
from conectar import *
from flask import request
from index import app

class Buscar():

    def __init__(self, id):
        self.id = id

    def buscar(self):

        db = conexion() 
        coleccion = db.libros.find_one({"_id": ObjectId(self.id)})
        documento = coleccion

        return documento
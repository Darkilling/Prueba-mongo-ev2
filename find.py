import json 
from bson import json_utilfrom conectar import *


db = conexion()
coleccion = db.evaluacion2
documentos = coleccion.find()
resultado = []

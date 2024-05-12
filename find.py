import json 
from bson import json_util
from conectar import *


db = conexion()
coleccion = db.evaluacion2
documentos = coleccion.find()
resultado = []

for documento in documentos:
    documento['_id'] = str(documento['_id'])
    resultado.append(documento)

print(json_util.dumps(resultado, indent=4))

import json 
from bson import json_util
from conectar import *


db = conexion()

coleccion_libros = db.libros
documentos_libros = coleccion_libros.find()
resultado_libros = []

for documento in documentos_libros:
    documento['_id'] = str(documento['_id'])
    resultado_libros.append(documento)


coleccion_autores = db.autores
documentos_autores = coleccion_autores.find()
resultado_autores = []

for documento in documentos_autores:
    documento['_id'] = str(documento['_id'])
    resultado_autores.append(documento)


coleccion_clientes = db.clientes
documentos_clientes = coleccion_clientes.find()
resultado_clientes = []

for documento in documentos_clientes:
    documento['_id'] = str(documento['_id'])
    resultado_clientes.append(documento)


coleccion_pedidos = db.pedidos
documentos_pedidos = coleccion_pedidos.find()
resultado_pedidos = []

for documento in documentos_pedidos:
    documento['_id'] = str(documento['_id'])
    resultado_pedidos.append(documento)

resultado = {
    'libros': resultado_libros,
    'autores': resultado_autores,
    'clientes': resultado_clientes,
    'pedidos': resultado_pedidos
}

print(json_util.dumps(resultado, indent=4))

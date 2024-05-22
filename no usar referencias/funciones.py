'''from conectar import conexion
from flask import request


@app.route('/insertar_cliente', methods=['POST'])
def insertar_cliente(id, nombre, email):
    db = conexion()
    coleccion = db.clientes

    nuevo_documento = {
        "_id": id,
        "nombre": nombre,
        "email": email
    }

    resultado = coleccion.insert_one(nuevo_documento)
    return resultado.inserted_id

def obtener_clientes():
    db = conexion()
    coleccion = db.clientes

    resultados = coleccion.find()
    return list(resultados)

def eliminar_cliente(id):
    db = conexion()
    coleccion = db.clientes

    resultado = coleccion.delete_one({"_id": id})
    return resultado.deleted_count
'''


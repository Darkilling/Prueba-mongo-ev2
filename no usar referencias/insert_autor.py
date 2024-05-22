'''from conectar import conexion
from flask import request
from index import app

def insertar_autor():
    db = conexion()
    coleccion = db.autores

    nombre = request.form.get('nombre')
    nacionalidad = request.form.get('nacionalidad')

    nuevo_documento = {
        "nombre": nombre,
        "nacionalidad": nacionalidad
    }

    resultado = coleccion.insert_one(nuevo_documento)

    print("El id del nuevo autor es:", resultado.inserted_id)'''